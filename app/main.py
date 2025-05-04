from fastapi import FastAPI, status
from mangum import Mangum
from dotflow import DotFlow

from app.serializers.telegram import Telegram
from app.tasks.task_telegram import task_telegram

app = FastAPI()


@app.post("/notify/telegram", status_code=status.HTTP_201_CREATED)
async def notify_telegram(item: Telegram):
    workflow = DotFlow()
    workflow.task.add(step=task_telegram, initial_context=item)
    workflow.start(mode="background")

    return {"message": "ok"}

handler = Mangum(app)
