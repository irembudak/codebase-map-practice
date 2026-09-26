from fastapi import APIRouter, HTTPException, status

from app.models.task import Task, TaskCreate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])
service = TaskService()


@router.post("", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    return service.create_task(payload)


@router.get("", response_model=list[Task])
def list_tasks() -> list[Task]:
    return service.list_tasks()


@router.patch("/{task_id}/complete", response_model=Task)
def complete_task(task_id: int) -> Task:
    task = service.complete_task(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    deleted = service.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
