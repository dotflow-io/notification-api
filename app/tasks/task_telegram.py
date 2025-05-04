import os

from json import dumps

from dotflow import action
from requests import post
from dotenv import load_dotenv


@action
def task_telegram(initial_context):
    load_dotenv()
    context = initial_context.storage

    response = post(
        url=f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage",
        headers={"Content-Type": "application/json"},
        data=dumps(
            {
                "chat_id": context.chat_id,
                "text": f"```json\n{context.task}```",
                "parse_mode": "markdown",
            }
        ),
    )
    response.raise_for_status()
