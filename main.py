# main.py
"""
Main entry point for the Weekly Task Scheduling System.
This program demonstrates our two-component pipeline:
1. Dynamic Programming (DP) for deadline-constrained task selection.
2. BFS-style time-slot mapping for weekly schedule construction.
"""

from task import Task
from dp_task_selection import select_tasks_with_deadlines_dp
from bfs_schedule_mapping import build_weekly_schedule_from_blocks


def print_selected_tasks(selected_tasks):
    print("\n=== Selected Tasks by Dynamic Programming ===")
    if not selected_tasks:
        print("No tasks selected.")
        return

    for task in selected_tasks:
        print(f"- {task.name} | Duration: {task.duration} hrs | "
              f"Deadline: Day {task.deadline_day} | Priority: {task.priority}")


def print_weekly_schedule(schedule, total_days):
    print("\n=== Weekly Schedule (BFS Time Mapping) ===")
    for day in range(1, total_days + 1):
        print(f"\nDay {day}:")
        if day not in schedule or len(schedule[day]) == 0:
            print("  (No tasks scheduled)")
            continue

        for hour, task_name in schedule[day]:
            print(f"  Hour {hour}: {task_name}")


def main():
    # Weekly parameters
    HOURS_PER_DAY = 6
    TOTAL_DAYS = 7

    # Sample tasks for demonstration
    tasks = [
        Task(1, "CS5800 Homework", duration=5, deadline_day=3, priority=10, dependencies=[]),
        Task(2, "Medical Project Report", duration=6, deadline_day=5, priority=9, dependencies=[1]),
        Task(3, "Resume Update", duration=2, deadline_day=4, priority=7, dependencies=[]),
        Task(4, "Internship Application", duration=3, deadline_day=7, priority=8, dependencies=[3]),
        Task(5, "Leetcode Practice", duration=4, deadline_day=7, priority=5, dependencies=[]),
    ]

    print("=== Weekly Task Scheduling System ===")

    # 1. Dynamic Programming: select tasks + build linear timeline
    selected_tasks, schedule_blocks = select_tasks_with_deadlines_dp(
        tasks, HOURS_PER_DAY, TOTAL_DAYS
    )

    print_selected_tasks(selected_tasks)

    # 2. BFS-style mapping: convert linear timeline → weekly schedule
    schedule = build_weekly_schedule_from_blocks(
        schedule_blocks, HOURS_PER_DAY, TOTAL_DAYS
    )

    print_weekly_schedule(schedule, TOTAL_DAYS)


if __name__ == "__main__":
    main()
