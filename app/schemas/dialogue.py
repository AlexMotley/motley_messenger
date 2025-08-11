from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class DialogueBase(BaseModel):
    title: str = Field(..., max_length=50, examples=["General Chat"])
    is_group: bool = Field(default=False, examples=[True])


class DialogueCreate(DialogueBase):
    participants_ids: List[UUID]  = Field(..., max_length=100)


class DialogueUpdate(DialogueBase):
    title: Optional[str] = Field(..., min_length=1, max_length=50)
    

class DialogueResponse(DialogueBase):
    id: int
    created_at:  datetime
    participant: List[UUID]

    class Config:
        from_attributes = True
