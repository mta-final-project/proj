import pandas as pd

from models import LECTURES_IDS, Column, Course, Lesson


def read_courses_file(path: str) -> pd.DataFrame:
    courses_df = pd.read_excel(path)
    courses_df = courses_df[Column.Credits].fillna(0)

    return courses_df


def init_courses_map(courses_file_datapath: str) -> dict[str, Course]:
    courses_map = {}
    courses_data = read_courses_file(courses_file_datapath)

    # Iterate through the DataFrame
    for index, row in courses_data.iterrows():
        # Get the current value
        curr_course = row[Column.Subject]

        # Check if the course is already in the map
        if curr_course not in courses_map:
            # If not, create a new Course object for this course
            courses_map[curr_course] = Course(
                department=row[Column.Department],
                subject=row[Column.Subject],
                credits=row[Column.Credits],
            )

        lesson = Lesson.from_row(row)

        if row[Column.CourseType] not in LECTURES_IDS:
            courses_map[curr_course].lectures.append(lesson)
        else:
            courses_map[curr_course].exercises.append(lesson)

    return courses_map


def main() -> None:
    data = init_courses_map("./input/coursesFile.xlsx")
    print(data)
    ...


if __name__ == "__main__":
    main()
