from typing import Self
from datetime import time, timedelta, datetime, date
from dataclasses import dataclass, field
from enum import Enum, StrEnum
import pandas as pd


LECTURES_IDS = [7, 13, 14, 15]


class Column(StrEnum):
    Group = "קבוצה"
    Subject = "תיאור נושא"
    Day = "יום בשבוע"
    Lecturer = "שם מרצה"
    StartTime = "שעת התחלה"
    EndTime = "שעת סיום"
    TotalHours = 'סה"כ שעות'
    Classroom = "תיאור כיתה"
    Department = "תיאור חוג"
    Credits = 'נ"ז'
    CourseType = "סוג מקצוע"


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


@dataclass
class Lesson:
    group: str
    subject: str
    day: Day
    lecturer: str
    start_time: time
    end_time: time
    classroom: str

    @classmethod
    def from_row(cls, row: pd.Series) -> Self:
        return cls(
            row[Column.Group],
            row[Column.Subject],
            row[Column.Day],
            row[Column.Lecturer],
            row[Column.StartTime],
            row[Column.EndTime],
            row[Column.Classroom],
        )

    @property
    def duration(self) -> timedelta:
        return datetime.combine(date.min, self.end_time) - datetime.combine(
            date.min, self.start_time
        )


@dataclass
class Course:
    department: str
    subject: str
    credits: int
    lectures: list[Lesson] = field(default_factory=list)
    exercises: list[Lesson] = field(default_factory=list)