from wbso_lib import event

meeting_type = 'meeting-standup'
training_story = 'Learning and Training'
training_type = 'training'
work_type = 'research-analysis'
work_story = 'User analysis'
hackathon_type = 'coding'
hackathon_story = 'Hackathon'


def get_events(*week_days):
    """Get events during the week.

    Args:
        *week_days (iterable<string>): Week days, starting Monday,
            formatted as required by the WBSO tool.
    Returns:
        events (iterable)
    """
    mon, tue, wed, thur, fri = week_days

    work_days = [mon, tue, wed, thur, fri]

    # Work.
    for day in work_days:
        yield event(date=day, type='planning', desc='Plan',
                    story=work_story, duration='60m')
        yield event(date=day, type=work_type,
                    desc='Action',
                    story=work_story, duration='360m')

    # Meetings
    yield event(date=wed, type=meeting_type, desc='One-on-one',
                story=work_story, duration='60m')
    yield event(date=mon, type=meeting_type, desc='Team planning meeting',
                story=work_story, duration='60m')
    stand_up_days = [tue, wed, thur]
    for day in stand_up_days:
        yield event(date=day, type=meeting_type, desc='Discussing work',
                    story=work_story, duration='30m')
    yield event(date=wed, type=meeting_type, desc='Knowledge sharing',
                story=work_story, duration='60m')
    # yield event(date=wed, type=meeting_type, desc='Retrospective',
    #             story=work_story, duration='120m')
    # yield event(date=fri, type=meeting_type, desc='Tech all-hands',
    #             story=work_story, duration='90m')
    yield event(date=fri, type=meeting_type, desc='FEA Highlights',
                story=work_story, duration='60m')

    # Talks
    yield event(date=mon, type=training_type, desc='Analytics talk',
                story=training_story, duration='40m')
    yield event(date=mon, type=training_type, desc='Machine learning talk',
                story=training_story, duration='60m')
    yield event(date=thur, type=training_type,
                desc='Experiment Tool Highlights sessions',
                story=training_story, duration='60m')

    # Training
    # yield event(date=fri, type=training_type,desc='How to use a computer',
    #             story=training_story, duration='300m')
