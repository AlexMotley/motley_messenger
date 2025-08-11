from app.db.base_class import BaseModel
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
import enum
from datetime import datetime


class DialogueParticipant(BaseModel):
    class RolesEnum(str, enum.Enum):
        ADMIN = 'admin'
        MEMBER = 'member'

    __tablename__ = 'dialogue_participants'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    dialogue_id: Mapped[int] = mapped_column(Integer, ForeignKey('dialogues.id', ondelete='CASCADE'), nullable=False)
    role: Mapped[RolesEnum] = mapped_column(String, default=RolesEnum.MEMBER, nullable=False)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    dialogue: Mapped['Dialogue'] = relationship(back_populates='participants')
    user: Mapped['User'] = relationship(back_populates='dialogues')
    