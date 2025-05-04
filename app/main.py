from fastapi import FastAPI, status
from mangum import Mangum
from dotflow import DotFlow

from app.notification import Notification
from app.tasks.notify_telegram import notify_telegram

app = FastAPI()


@app.post("/notify/telegram", status_code=status.HTTP_201_CREATED)
async def post_notify_telegram(item: Notification):
    workflow = DotFlow()
    workflow.task.add(step=notify_telegram, initial_context=item)
    workflow.start(mode="background")

    return {"message": "ok"}

handler = Mangum(app)
