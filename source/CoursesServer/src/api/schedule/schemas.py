from pydantic import BaseModel
from beanie import PydanticObjectId


class GetCombiSchema(BaseModel):
    selected_courses: list[PydanticObjectId]
