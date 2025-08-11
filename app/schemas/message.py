from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class MessageBase(BaseModel):
    text: str = Field(..., max_length=1000)


class MessageCreate(MessageBase):
    dialogue_id: int = Field(..., examples=[1], description="ID диалога, куда отправляется сообщение.")
    

class MessageResponse(MessageBase):
    id: int
    sender_id: UUID
    dialogue_id: int
    send_date: datetime

    class Config:
        from_attributes = True
