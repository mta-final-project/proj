from datetime import time
from enum import StrEnum

from beanie import Document
from pydantic import BaseModel


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


class Lesson(BaseModel):
    group: str
    subject: str
    day: int
    lecturer: str
    start_time: time
    end_time: time
    classroom: str


class Course(Document):
    department: str
    subject: str
    credit: int
    description: str
    lectures: list[Lesson]
    exercises: list[Lesson]
