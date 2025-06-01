from datetime import time

# Define the Task Class
class Task:
    def __init__(self, task_name: str, task_time: time, task_description: str=""):
        self.task_name = task_name
        self.task_time = task_time # Receives a datetime.time object
        self.task_description = task_description

    def __repr__(self):
        return f"<Task(name={self.task_name}, time={self.task_time}, description={self.task_description})>"

# Define the Schedule Class
class Schedule:
    def __init__(self, schedule_name: str):
        self.schedule_name = schedule_name
        self.schedule_tasks = [] # List of Task Objects
    
    def add_task(self, task: Task):
        self.schedule_tasks.append(task)

    def remove_task(self, task: str):
        self.schedule_tasks = [i for i in self.schedule_tasks if i.task_name != task]

    def get_task(self, task_name: str):
        for task in self.schedule_tasks:
            if task.schedule_name == task_name:
                return task
        return None
    
    def __repr__(self):
        return f"<Schedule(name={self.schedule_name}, tasks={len(self.schedule_tasks)})>"