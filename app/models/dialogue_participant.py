from app.db.base_class import BaseModel
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from datetime import datetime
from typing import List


class DialogueParticipant(BaseModel):
    class Roles:
        ADMIN: str = 'admin'
        MEMBER: str = 'member'

    __tablename__ = 'dialogue_participants'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    dialog_id: Mapped[int] = mapped_column(Integer, ForeignKey('dialogues.id', ondelete='CASCADE'), nullable=False)
    role: Mapped[str] = mapped_column(String, default=Roles.MEMBER, nullable=False)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    dialogue: Mapped['Dialogue'] = relationship(back_populates='participants')
    user: Mapped['User'] = relationship(back_populates='dialogues')
    