from app.models.task import Task, TaskCreate


class TaskRepository:
    """Stores tasks in memory for this practice project."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def create(self, payload: TaskCreate) -> Task:
        task = Task(
            id=self._next_id,
            title=payload.title,
            description=payload.description,
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def mark_complete(self, task_id: int) -> Task | None:
        task = self._tasks.get(task_id)

        if task is None:
            return None

        completed_task = task.model_copy(update={"completed": True})
        self._tasks[task_id] = completed_task
        return completed_task

    def delete(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True
