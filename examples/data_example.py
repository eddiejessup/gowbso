from gowbso import WEEK_DAY_NAMES, WBSOWriter

meeting_type = 'meeting-standup'
training_story = 'Learning and Training'
training_type = 'training'
work_type = 'research-analysis'
work_story = 'User analysis'
hackathon_type = 'coding'
hackathon_story = 'Hackathon'


mon, tue, wed, thur, fri = WEEK_DAY_NAMES
wbso = WBSOWriter()

# Work.
for day in WEEK_DAY_NAMES:
    wbso.add(day=day, type_='planning', desc='Plan',
             story=work_story, duration='60m')
    wbso.add(day=day, type_=work_type,
             desc='Action',
             story=work_story, duration='360m')

# Meetings
wbso.add(day=wed, type_=meeting_type, desc='One-on-one',
         story=work_story, duration='60m')
wbso.add(day=mon, type_=meeting_type, desc='Team planning meeting',
         story=work_story, duration='60m')
stand_up_days = [tue, wed, thur]
for day in stand_up_days:
    wbso.add(day=day, type_=meeting_type, desc='Discussing work',
             story=work_story, duration='30m')
wbso.add(day=wed, type_=meeting_type, desc='Knowledge sharing',
         story=work_story, duration='60m')
# wbso.add(day=wed, type_=meeting_type, desc='Retrospective',
#          story=work_story, duration='120m')
# wbso.add(day=fri, type_=meeting_type, desc='Tech all-hands',
#          story=work_story, duration='90m')
wbso.add(day=fri, type_=meeting_type, desc='FEA Highlights',
         story=work_story, duration='60m')

# Talks
wbso.add(day=mon, type_=training_type, desc='Analytics talk',
         story=training_story, duration='40m')
wbso.add(day=mon, type_=training_type, desc='Machine learning talk',
         story=training_story, duration='60m')
wbso.add(day=thur, type_=training_type,
         desc='Experiment Tool Highlights sessions',
         story=training_story, duration='60m')

# Training
# wbso.add(day=fri, type_=training_type,desc='How to use a computer',
#          story=training_story, duration='300m')

wbso.write()
