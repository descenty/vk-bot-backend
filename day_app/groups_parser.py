import json

from day_app.models import StudyGroup, ScheduleWeek, Subject, Teacher
import day_app.parsers
from day_app.parsers.schedule import GroupSchedule, week_days
from day_app.models import *
import pickle


def load_study_group(name: str):
    with open('day_app/parsers/groups_data', 'rb') as f:
        data = pickle.load(f)
        group_schedules: list[GroupSchedule] = data
    if name not in [x.name for x in group_schedules]:
        return False
    base_study_group = [x for x in group_schedules if x.name == name][0]
    study_group = StudyGroup(name=base_study_group.name)
    study_group.save()
    for schedule_week_count in range(1, 18):
        schedule_week = ScheduleWeek(count=schedule_week_count, study_group=study_group)
        schedule_week.save()
        for base_day in base_study_group.schedule_days:
            schedule_day = ScheduleDay(count=week_days.index(base_day.name) + 1, schedule_week=schedule_week)
            schedule_day.save()
            subject: Subject
            for base_subject_count in base_day.periods_subjects.keys():
                base_subject: day_app.parsers.schedule
                if schedule_week_count % 2 == 0:
                    base_subject = base_day.periods_subjects[base_subject_count][1]
                else:
                    base_subject = base_day.periods_subjects[base_subject_count][0]
                if base_subject is not None and (
                        base_subject.on_weeks is None or schedule_week_count in base_subject.on_weeks or (
                        base_subject.test_weeks is not None and schedule_week_count in base_subject.test_weeks)):
                    if base_subject.test_weeks is not None and schedule_week_count in base_subject.test_weeks:
                        form = 'кр.'
                    else:
                        form = base_subject.form
                    if base_subject.teacher is None:
                        if Teacher.objects.filter(name='undefined').count() == 0:
                            teacher = Teacher.objects.create(name='undefined')
                        else:
                            teacher = Teacher.objects.get(name='undefined')
                    elif Teacher.objects.filter(name__contains=base_subject.teacher).count() == 0:
                        teacher = Teacher.objects.create(name=base_subject.teacher)
                    else:
                        teacher = Teacher.objects.filter(name__contains=base_subject.teacher).first()
                    teacher.save()
                    subject = Subject(name=base_subject.name,
                                      form=form, teacher=teacher,
                                      audience_name=base_subject.audience_name,
                                      count=base_subject_count + 1, schedule_day=schedule_day)
                else:
                    subject = Subject(name=None, count=base_subject_count + 1, schedule_day=schedule_day)
                subject.save()
    return True
