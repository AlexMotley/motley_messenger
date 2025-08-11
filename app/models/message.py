from app.db.base_class import BaseModel
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Uuid, String, DateTime, Integer, ForeignKey
from datetime import datetime
import uuid
from typing import List


class Message(BaseModel):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    text: Mapped[str] = mapped_column(String(1000), nullable=False)
    sender_uuid: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    dialogue_id: Mapped[int] = mapped_column(Integer, ForeignKey('dialogues.id', ondelete='CASCADE'), nullable=False)
    send_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    sender: Mapped['User'] = relationship(back_populates='messages')
    dialogue: Mapped['Dialogue'] = relationship(back_populates='messages')
    attachments: Mapped[List['Attachment']] = relationship(back_populates='message')
