from typing import Self
from datetime import time, timedelta, datetime, date
from dataclasses import dataclass, field
from enum import Enum, StrEnum
import pandas as pd

# TODO
# set credits to 0 if there's no value


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


def read_courses_file(datapath: str) -> pd.DataFrame:
    # TODO the function should the path as a param, not hardcoded value- DONE
    courses_table_datapath = datapath
    courses_data = pd.read_excel(courses_table_datapath)
    return courses_data


def init_courses_map(courses_file_datapath: str) -> dict[str, Course]:
    courses_map = {}
    courses_data = read_courses_file(courses_file_datapath)

    # Iterate through the DataFrame
    for index, row in courses_data.iterrows():
        # Get the current value
        # TODO i think those comment (with column names) are redundant since anyone can easily look at the enum definition -DONE
        curr_course = row[Column.Subject]  

        # Check if the course is already in the map
        if curr_course not in courses_map:
            # If not, create a new Course object for this course
            courses_map[curr_course] = Course(
                department=row[Column.Department],   
                subject=row[Column.Subject],
                credits=row[Column.Credits],  
            )

        # If the course type is not None and is a lecture or exercise, add it to the respective list - i did not understand
        # TODO magic numbers, should be defined somewhere else, not in the middle of the func -where should i define them? 
        lesson = Lesson.from_row(row)

        if row[Column.CourseType] not in [7, 13, 14, 15]:
            courses_map[curr_course].lectures.append(lesson)
        else:
            courses_map[curr_course].exercises.append(lesson)

    return courses_map


def main():
    courses = init_courses_map("./input/coursesFile.xlsx")
    # TODO even if only used for debugging purposes, this code does not need to be here. it won't be used in the final script.
    # i don't mean you shouldn't have write it, but maybe don't commit it, or maybe write it in a separate script that you don't intend to commit
    # when committing code with any (decent) ide, it should give you the option to choose which changes to include in the commit
    # (even between changes within the same file)
    with open("output.txt", "w") as file:
        for course_name, course in courses.items():
            file.write(
                f"--------------------------------Course: {course_name} ------------------------------------\n"
            )
            file.write(f"Department: {course.department}\n")
            file.write(f"Credits: {course.credits}\n")
            file.write("Lectures:\n")
            for lecture in course.lectures:
                file.write(f"Group: {lecture.group}\n")
                file.write(f"Subject: {lecture.subject}\n")
                file.write(f"Day: {lecture.day}\n")
                file.write(f"Lecturer: {lecture.lecturer}\n")
                file.write(f"Start Time: {lecture.start_time}\n")
                file.write(f"End Time: {lecture.end_time}\n")
                file.write(f"Duration: {lecture.duration}\n")
                file.write(f"Classroom: {lecture.classroom}\n")
                file.write("\n")
            file.write(
                "--------------------------------Exercises:------------------------------------\n"
            )
            for exercise in course.exercises:
                file.write(f"Group: {exercise.group}\n")
                file.write(f"Subject: {exercise.subject}\n")
                file.write(f"Day: {exercise.day}\n")
                file.write(f"Lecturer: {exercise.lecturer}\n")
                file.write(f"Start Time: {exercise.start_time}\n")
                file.write(f"End Time: {exercise.end_time}\n")
                file.write(f"Duration: {exercise.duration}\n")
                file.write(f"Classroom: {exercise.classroom}\n")
                file.write("\n")
            file.write("\n")


if __name__ == "__main__":
    main()
