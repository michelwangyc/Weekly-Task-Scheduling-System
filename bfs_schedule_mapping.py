from collections import defaultdict
from typing import Dict

def build_weekly_schedule_from_blocks(schedule_blocks,
                                      hours_per_day,
                                      total_days):
    """
    Converts linear time blocks into a weekly schedule.

    Returns:
      schedule: dict mapping day -> list of (hour_in_day, task_name)
    """
    schedule = defaultdict(list)

    for (start, end, task) in schedule_blocks:
        for slot in range(start, end):
            day = slot // hours_per_day + 1
            hour_in_day = slot % hours_per_day

            if day <= total_days:
                schedule[day].append((hour_in_day, task.name))

    # Sort hours within each day
    for day in schedule:
        schedule[day].sort(key=lambda x: x[0])

    return schedule
