from datetime import time

from pydantic import BaseModel, Field


class TimeSlot(BaseModel):
    day: int = Field(..., ge=1, le=7)  # TODO duplication, maybe create a new pydantic type?
    start_time: time
    end_time: time
