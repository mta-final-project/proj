import io

import pandas as pd

from src.app.models import Column, Course, Lesson

LECTURES_IDS = [7, 13, 14, 15]
DAY_OF_WEEK_MAP = {"א": 1, "ב": 1, "ג": 1, "ד": 1, "ה": 1, "ו": 1}


async def list_courses() -> list[Course]:
    return await Course.find_all().to_list()


async def delete_courses() -> None:
    await Course.delete_all()


async def upload_courses(data: bytes):
    df = _read_excel(io.BytesIO(data))
    courses = _extract_courses(df)
    _fill_course_lessons(df, courses)

    await _save_courses(list(courses.values()))


def _read_excel(bytes_io: io.BytesIO) -> pd.DataFrame:
    courses_df = pd.read_excel(bytes_io)
    courses_df[Column.Credits] = courses_df[Column.Credits].fillna(0)
    courses_df[Column.Classroom] = courses_df[Column.Classroom].fillna("")
    courses_df[Column.Lecturer] = courses_df[Column.Lecturer].fillna("")
    courses_df[Column.Day] = courses_df[Column.Day].map(DAY_OF_WEEK_MAP)
    # TODO check why there are NaNs

    return courses_df


def _extract_courses(courses_df: pd.DataFrame) -> dict[str, Course]:
    courses = {}
    for _, row in courses_df.iterrows():
        subject = row[Column.Subject]
        course = Course(
            department=row[Column.Department],
            subject=subject,
            credit_points=row[Column.Credits],
        )
        courses[subject] = course

    return courses


def _fill_course_lessons(courses_df: pd.DataFrame, courses: dict[str, Course]) -> None:
    for _, row in courses_df.iterrows():
        lesson = Lesson.from_row(row)
        subject = row[Column.Subject]
        course = courses[subject]

        if row[Column.LessonType] not in LECTURES_IDS:
            course.lectures.append(lesson)
        else:
            course.exercises.append(lesson)


async def _save_courses(courses: list[Course]) -> None:
    await Course.delete_all()

    for course in courses:
        await course.save()
