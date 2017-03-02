import argparse
from collections import namedtuple, Mapping
import csv
import sys

import arrow


def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


# story, topic: Your current work, where 'story' is more general than 'topic'.
field_names = ['date', 'type', 'desc', 'story', 'duration', 'status',
               'details']
event = namedtuple_with_defaults('event', field_names,
                                 default_values={'status': None,
                                                 'details': None})


def get_monday():
    today = arrow.now()
    monday = today.replace(days=-today.weekday())
    # If today is Thursday or before, we probably want *last* monday.
    # Because what sort of crazy person would be doing this horrible thing
    # more than once a week?
    if today.weekday() <= 3:
        monday = monday.replace(weeks=-1)
    return monday


def write_events(events):
    # Sort events by time, for ease of inspection and editing.
    events = sorted(events, key=lambda event: event.date)
    # Write to standard-out.
    csv_writer = csv.DictWriter(sys.stdout, fieldnames=field_names)
    csv_writer.writeheader()
    for event in events:
        csv_writer.writerow(event._asdict())


def valid_monday(s):
    """Convert a string to a date, and check it is a Monday.."""
    d = arrow.get(s)
    if d.weekday() > 0:
        raise argparse.ArgumentTypeError('Not a monday')
    return d


def monday_to_week_days(monday):
    week_days = [monday.replace(days=+i) for i in range(5)]
    return (day.format('YYYY-MM-DD') for day in week_days)
