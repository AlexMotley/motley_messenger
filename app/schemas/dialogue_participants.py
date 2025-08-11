from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class DialogueParticipantBase(BaseModel):
    role: str = Field(..., examples=['member'])


class DialogueParticipantCreate(DialogueParticipantBase):
    user_id: UUID = Field(..., )
    dialogue_id: int = Field(..., examples=[1])


class DialogueParticipantUpdate(DialogueParticipantBase):
    role: Optional[str] = Field(None, examples=['member'])
    joined_at: Optional[datetime] = Field(None, examples=['2024-01-01'])


class DialogueParticipantResponse(DialogueParticipantBase):
    id: int
    user_id: UUID
    dialogue_id: int
    joined_at: datetime

    class Config():
        from_attributes = True
