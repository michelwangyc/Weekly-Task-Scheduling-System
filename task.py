# task.py

from dataclasses import dataclass

@dataclass
class Task:
    id: int
    name: str
    duration: int          # total hours needed
    deadline_day: int      # 1..7
    priority: int          # importance level
