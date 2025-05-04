from typing import Dict, Any

from pydantic import BaseModel


class Telegram(BaseModel):
    chat_id: int
    task: Dict[str, Any]
