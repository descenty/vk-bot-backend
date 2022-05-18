from dataclasses import dataclass

week_days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
periods = (('9-00', '10-30'), ('10-40', '12-10'),
           ('12-40', '14-10'), ('14-20', '15-50'),
           ('16-20', '17-50'), ('18-00', '19-30'))


@dataclass
class Subject:
    name: str
    form: str
    teacher: str
    audience_name: str
    on_weeks: list[int]
    test_weeks: list[int]

    def encode(self):
        return self.__dict__


@dataclass
class ScheduleDay:
    name: str
    periods_subjects: dict[int:tuple[Subject]]

    def encode(self):
        return self.__dict__


@dataclass
class GroupSchedule:
    name: str
    schedule_days: list[ScheduleDay]

    def encode(self):
        return self.__dict__
