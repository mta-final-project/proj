from datetime import time
from enum import StrEnum

from beanie import Document
from pydantic import BaseModel, Field


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
    day: int = Field(..., ge=1, le=7)
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
