from beanie import PydanticObjectId
from pydantic import BaseModel


class GroupViewSchema(BaseModel):
    course_id: PydanticObjectId
    group: int
    description: str
    lecturer: str


class SelectedGroupsSchema(BaseModel):
    groups: list[GroupViewSchema]
