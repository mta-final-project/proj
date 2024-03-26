from fastapi import APIRouter, status, Query
from beanie import PydanticObjectId

from src.api.schedule.schemas import SelectedGroupsSchema, GroupViewSchema
from src.apps.courses.models import Course
from src.apps.shcedule import service

router = APIRouter(prefix="/schedule", tags=["Schedule"])


@router.get("/combinations", status_code=status.HTTP_200_OK)
async def get_combinations(
        courses_ids: list[PydanticObjectId] = Query(default=None)
) -> list[SelectedGroupsSchema]:

    courses_ids = courses_ids or []
    courses = [await Course.get(_id) for _id in courses_ids]

    options = service.get_optional_combinations(courses)
    result = []
    for option in options:
        groups = [
            GroupViewSchema(**dict(group), course_id=course_id)
            for group, course_id in zip(option, courses_ids)
        ]
        result.append(SelectedGroupsSchema(groups=groups))

    return result
