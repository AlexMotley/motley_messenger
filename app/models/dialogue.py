from typing import List
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import BaseModel


class Dialogue(BaseModel):
    __tablename__ = 'dialogues'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    is_group: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    
    messages: Mapped[List['Message']] = relationship(back_populates='dialogue')
    participants: Mapped[List["DialogueParticipant"]] = relationship(back_populates='dialogue')
    