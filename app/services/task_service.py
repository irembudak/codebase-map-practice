from app.models.task import Task, TaskCreate
from app.repositories.task_repository import TaskRepository
from app.utils.validation import normalize_title


class TaskService:
    """Contains task-related business rules."""

    def __init__(self, repository: TaskRepository | None = None) -> None:
        self.repository = repository or TaskRepository()

    def create_task(self, payload: TaskCreate) -> Task:
        normalized = payload.model_copy(
            update={"title": normalize_title(payload.title)}
        )
        return self.repository.create(normalized)

    def list_tasks(self) -> list[Task]:
        return self.repository.list_all()

    def complete_task(self, task_id: int) -> Task | None:
        return self.repository.mark_complete(task_id)

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
