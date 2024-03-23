from datetime import date, datetime, time, timedelta
from enum import StrEnum
from typing import Self

import pandas as pd
from beanie import Document
from pydantic import BaseModel, Field


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
    day: int = Field(..., ge=1, le=7)
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


class Group(BaseModel):
    group: int
    description: str
    lecturer: str
    lessons: list[Lesson] = Field(default_factory=list)

    @classmethod
    def from_row(cls, row: pd.Series) -> Self:
        return cls(
            group=row[Column.Group],
            description=row[Column.GroupDescription],
            lecturer=row[Column.Lecturer],
        )


class Course(Document):
    semester: int = Field(..., ge=1, le=3)
    department: str
    subject: str
    credit_points: int
    lectures: list[Group] = Field(default_factory=list)
    exercises: list[Group] = Field(default_factory=list)

    class Settings:
        bson_encoders = {time: str}

    @classmethod
    def from_row(cls, row: pd.Series) -> Self:
        return cls(
            semester=row[Column.Semester],
            department=row[Column.Department],
            subject=row[Column.Subject],
            credit_points=row[Column.Credits],
        )

    @property
    def number_of_lectures(self) -> int:
        return len(self.lectures)

    @property
    def number_of_exercises(self) -> int:
        return len(self.exercises)
