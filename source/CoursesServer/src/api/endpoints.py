from fastapi import APIRouter, HTTPException, UploadFile, status

from src.app.models import Course
from src.app.service import list_courses, upload_courses

router = APIRouter(prefix="/courses")


@router.get("", status_code=status.HTTP_200_OK)
async def list_courses() -> list[Course]:
    return await list_courses()


@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def upload_courses(file: UploadFile):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file should be an .xlsx file",
        )

    contents = await file.read()
    await upload_courses(contents)
