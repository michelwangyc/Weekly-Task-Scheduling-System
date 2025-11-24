from dataclasses import dataclass
from typing import List

##Zhenyu Wang
@dataclass
class Task:
    id: int
    name: str
    duration: int          # total hours needed
    deadline_day: int      # 1-7
    priority: int          # 1- 10 larger = more important
    dependencies: List[int]
