from src.apps.courses.models import Course, Group
from src.apps.shcedule.schedule import Schedule, TimeSlot

type SelectedGroups = list[Group]
type Option = tuple[SelectedGroups, Schedule]


def get_optional_combinations(courses: list[Course]) -> list[SelectedGroups]:
    options = [([], Schedule())]  # add a single option with no groups and empty schedule

    for course in courses:
        options = _update_options(options, course.lectures)
        options = _update_options(options, course.exercises)

    return [selected_groups for selected_groups, _ in options]


def _update_options(options: list[Option], groups: list[Group]) -> list[Option]:
    if not groups:
        return options

    new_schedules, new_groups = [], []
    for option, schedule in options:
        new_schedule = schedule.copy()
        for group in groups:
            try:
                _add_group_to_schedule(new_schedule, group)
                new_schedules.append(new_schedule)
                new_groups.append(option + [group])
            except ValueError:
                continue

    return list(zip(new_groups, new_schedules))


def _add_group_to_schedule(schedule: Schedule, group: Group) -> None:
    for lesson in group.lessons:
        schedule.add_lesson(TimeSlot(**dict(lesson)))
