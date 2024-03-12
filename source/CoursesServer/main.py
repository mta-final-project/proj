from datetime import time, timedelta, datetime, date
from dataclasses import dataclass
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
    TotalHours = "סה\"כ שעות"
    Classroom = "תיאור כיתה"
    Department = "תיאור חוג"
    Credits = "נ\"ז"
    CourseType = "סוג מקצוע"



class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


class Course:
    def __init__(self, department, subject, credits, lectures=None, exercises=None):
        self.department = department
        self.subject = subject
        self.credits = credits
        self.lectures = []
        self.exercises = []

    def add_lecture(self, row) -> None:
        self.lectures.append(
            Lesson(row[Column.Group], row[Column.Subject], row[Column.Day], row[Column.Lecturer], row[Column.StartTime],
                   row[Column.EndTime], row[Column.Classroom]))

    def add_exercise(self, row) -> None:
        self.exercises.append(
            Lesson(row[Column.Group], row[Column.Subject], row[Column.Day], row[Column.Lecturer], row[Column.StartTime],
                   row[Column.EndTime], row[Column.Classroom]))


@dataclass
class Lesson:
    group: str
    subject: str
    day: Day
    lecturer: str
    start_time: time
    end_time: time
    classroom: str

    @property
    def duration(self) -> timedelta:
        return datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time)


def read_courses_file() -> pd.DataFrame: 
    courses_table_datapath = "./input/coursesFile.xlsx"
    courses_data = pd.read_excel(courses_table_datapath)
    return courses_data


def init_courses_map() -> dict[str, Course]:
    courses_map = {}

    courses_data = read_courses_file()

    # Iterate through the DataFrame
    for index, row in courses_data.iterrows():
        # Get the current value
        curr_course = row['תיאור נושא'] # שם הקורס

        # Check if the course is already in the map
        if curr_course not in courses_map:
            # If not, create a new Course object for this course
            courses_map[curr_course] = Course(
                department=row['תיאור חוג'],
                subject=row['תיאור נושא'], # שם הקורס
                credits=row['נ"ז']
            )

        # If the course type is not None and is a lecture or exercise, add it to the respective list
        if row['סוג מקצוע'] not in [7,13,14,15]:
            courses_map[curr_course].add_lecture(row)
        else:
            courses_map[curr_course].add_exercise(row)

    return courses_map


def main():
    courses = init_courses_map()
    with open('output.txt', 'w') as file:
        for course_name, course in courses.items():
            file.write(f"--------------------------------Course: {course_name} ------------------------------------\n")
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
            file.write("--------------------------------Exercises:------------------------------------\n")
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
