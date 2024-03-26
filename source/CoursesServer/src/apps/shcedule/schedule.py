from typing import Self

from src.apps.shcedule.models import TimeSlot


class Schedule:
    def __init__(self):
        self.lessons = {i: [] for i in range(1, 8)}

    def copy(self) -> Self:
        new_schedule = Schedule()
        for day, lessons in self.lessons.items():
            for lesson in lessons:
                new_schedule.add_lesson(lesson.copy())

        return new_schedule

    def is_available(self, time_slot: TimeSlot) -> bool:
        for lesson in self.lessons[time_slot.day]:
            if lesson.start_time <= time_slot.start_time < lesson.end_time:
                return False
            if lesson.start_time < time_slot.end_time <= lesson.end_time:
                return False

        return True

    def add_lesson(self, time_slot: TimeSlot) -> None:
        if not self.is_available(time_slot):
            raise ValueError("Time slot is not available")

        self.lessons[time_slot.day].append(time_slot)
