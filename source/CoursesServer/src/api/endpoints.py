from fastapi import APIRouter, status, UploadFile, HTTPException

from src.app.models import Course

router = APIRouter(prefix="courses")


@router.get("", status_code=status.HTTP_200_OK)
async def list_courses() -> list[Course]:
    return await Course.find_all().to_list()


@router.post("", responses=status.HTTP_204_NO_CONTENT)
async def upload_courses(file: UploadFile):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file should be an .xlsx file",
        )

    contents = await file.read()
    # TODO call parsing script
