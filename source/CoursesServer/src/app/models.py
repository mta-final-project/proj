from datetime import time

from beanie import Document
from pydantic import BaseModel


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
