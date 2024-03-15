import pandas as pd

from models import Course, Lesson, Column, LECTURES_IDS


# TODO
# set credits to 0 if there's no value


def read_courses_file(data_path: str) -> pd.DataFrame:
    courses_table_data_path = data_path
    courses_data = pd.read_excel(courses_table_data_path)
    return courses_data


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
