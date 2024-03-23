from fastapi import APIRouter

from src.api.courses.endpoints import router as courses_router

router = APIRouter()
router.include_router(courses_router)
