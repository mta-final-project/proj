from main import init_courses_map


def read_and_create_output_file():
    courses = init_courses_map("./input/coursesFile.xlsx")
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
    read_and_create_output_file()
