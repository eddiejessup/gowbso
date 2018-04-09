import csv
import sys

import arrow


WEEK_DAY_NAMES = {
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
}

FIELD_NAMES = ['date', 'type', 'desc', 'story', 'duration', 'status',
               'details']


def monday_to_week_days(monday):
    return (monday.replace(days=+i).format('YYYY-MM-DD') for i in range(5))


class WBSOWriter:

    def __init__(self, monday=None):
        if monday is None:
            self.monday = self.default_monday
        else:
            self.monday = arrow.get(monday)
            if self.monday.weekday() > 0:
                raise ValueError('Not a monday')
        self.events = []

    @property
    def week_days(self):
        return monday_to_week_days(self.monday)

    @property
    def week_day_map(self):
        return dict(zip(WEEK_DAY_NAMES, self.week_days))

    def _date_from_day_str(self, s):
        matches = [
            v
            for k, v in self.week_day_map.items()
            if k.startswith(s.lower())
        ]
        if not matches:
            raise ValueError('Did not understand day string, no matches')
        elif len(matches) > 1:
            raise ValueError(f'Day string ambiguous: matched: {matches}')
        else:
            return matches[0]

    def add(self, day, type_, story, duration, desc='', status=None,
            details=None):
        date = self._date_from_day_str(day)
        ev = dict(date=date, type=type_, desc=desc,
                  story=story, duration=duration)
        self.events.append(ev)

    @property
    def default_monday(self):
        today = arrow.now()
        monday = today.replace(days=-today.weekday())
        # If today is Thursday or before, we probably want *last* monday.
        # Because what sort of crazy person would be doing this horrible thing
        # more than once a week?
        if today.weekday() <= 3:
            monday = monday.replace(weeks=-1)
        return monday

    @property
    def events_by_date(self):
        return sorted(self.events, key=lambda event: event['date'])

    def write(self, stream=sys.stdout):
        csv_writer = csv.DictWriter(stream, fieldnames=FIELD_NAMES)
        csv_writer.writeheader()
        # Sort events by time, for ease of inspection and editing.
        csv_writer.writerows(self.events_by_date)
