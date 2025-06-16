from fastapi import BackgroundTasks
from abc import ABC, abstractmethod

class BackgroundTaskQueue(ABC):
    @abstractmethod
    def add_task(self, func, *args, **kwargs):
        pass

# TODO: separate this out into a separate file when needed
class FastAPIBackgroundTaskQueue(BackgroundTaskQueue):
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    def add_task(self, func, *args, **kwargs):
        self.background_tasks.add_task(func, *args, **kwargs)
