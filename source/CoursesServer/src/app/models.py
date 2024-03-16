from datetime import time

from beanie import Document, Link, BackLink


class Lesson(Document):
    group: str
    subject: str
    day: int
    lecturer: str
    start_time: time
    end_time: time
    classroom: str

    course: BackLink["Course"]


class Course(Document):
    department: str
    subject: str
    credit: int
    description: str
    lectures: list[Link[Lesson]]
    exercises: list[Link[Lesson]]
