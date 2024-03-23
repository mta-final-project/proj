from typing import Annotated

from fastapi import APIRouter, status, Depends

from src.api.schedule.schemas import GetCombiSchema as _GetCombiSchema

router = APIRouter(prefix="/schedule")

GetCombiSchema = Annotated[_GetCombiSchema, Depends(_GetCombiSchema)]


@router.get("/combinations", status_code=status.HTTP_200_OK)
async def get_combinations(params: GetCombiSchema):
    ...
