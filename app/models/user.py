from app.db.base_class import BaseModel
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Uuid, String, DateTime
from datetime import datetime
import uuid
from typing import List


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(70), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    account_name: Mapped[str] = mapped_column(String(70), unique=True, nullable=False)
    date_joined: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    
    messages: Mapped[List['Message']] = relationship(back_populates='sender')
    dialogues: Mapped[List['DialogueParticipants']] = relationship(back_populates='user')
