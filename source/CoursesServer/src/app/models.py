from typing import Self
from datetime import time, date, datetime, timedelta
from enum import StrEnum

from beanie import Document
from pydantic import BaseModel, Field
import pandas as pd


class Column(StrEnum):
    Group = "קבוצה"
    Subject = "תיאור נושא"
    GroupDescription = "מלל חופשי לתלמיד"
    LessonType = "סוג מקצוע"
    Semester = "סמסטר"
    Lecturer = "שם מרצה"
    Day = "יום בשבוע"
    StartTime = "שעת התחלה"
    EndTime = "שעת סיום"
    TotalHours = 'סה"כ שעות'
    Classroom = "תיאור כיתה"
    Credits = 'נ"ז'
    Department = "תיאור חוג"


class Lesson(BaseModel):
    group: int
    day: int = Field(..., ge=1, le=7)
    lecturer: str
    start_time: time
    end_time: time
    classroom: str

    @classmethod
    def from_row(cls, row: pd.Series) -> Self:
        return cls(
            group=row[Column.Group],
            day=row[Column.Day],
            lecturer=row[Column.Lecturer],
            start_time=row[Column.StartTime],
            end_time=row[Column.EndTime],
            classroom=row[Column.Classroom],
        )

    @property
    def duration(self) -> timedelta:
        return datetime.combine(date.min, self.end_time) - datetime.combine(
            date.min, self.start_time
        )


class Course(Document):
    department: str
    subject: str
    credit_points: int
    lectures: list[Lesson] = Field(default_factory=list)
    exercises: list[Lesson] = Field(default_factory=list)

    class Settings:
        bson_encoders = {time: str}
