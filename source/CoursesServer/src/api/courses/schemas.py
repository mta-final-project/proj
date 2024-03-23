from pydantic import BaseModel


class CourseViewSchema(BaseModel):
    semester: int
    department: str
    subject: str
    credit_points: int
    number_of_lectures: int
    number_of_exercises: int
