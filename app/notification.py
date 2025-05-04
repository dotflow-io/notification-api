from typing import Dict, Any

from pydantic import BaseModel


class Notification(BaseModel):
    chat_id: int
    task: Dict[str, Any]
