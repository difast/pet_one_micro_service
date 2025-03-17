from celery import Celery
import os

celery = Celery(
    __name__,
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND")
)

@celery.task
def process_task(task_id: int):
    return f"Processed task {task_id}"