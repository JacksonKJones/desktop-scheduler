import json
from models import Task, Schedule
from datetime import datetime

def save_schedule(schedule: Schedule, filename: str):
    data = {
        "name": schedule.schedule_name,
        "tasks": [
            {
                "name": task.task_name,
                "task_time": task.task_time.strftime("%H:%M"),
                "description": task.task_description
            }
            for task in schedule.schedule_tasks
        ]
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_schedule(filename: str) -> Schedule:
    with open(filename, 'r') as f:
        data = json.load(f)

    schedule = Schedule(data["name"])
    for task_data in data["tasks"]:
        task_time = datetime.strptime(task_data["task_time"], "%H:%M").time()
        task = Task(task_data["name"], task_time, task_data["description"])
        schedule.add_task(task)

    return schedule