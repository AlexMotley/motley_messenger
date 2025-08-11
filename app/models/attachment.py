from app.db.base_class import BaseModel
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from datetime import datetime
from typing import List


class Attachment(BaseModel):
    class FileTypes:
        FILE = 'file'
        IMAGE = 'image'
        AUDIO = 'audio'
        VIDEO = 'video'

    __tablename__ = 'attachments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id", ondelete="CASCADE"), nullable=False)
    type: Mapped[str] = mapped_column(String(5))
    url: Mapped[str] = mapped_column(String(512))
    filename: Mapped[str] = mapped_column(String(255))

    message: Mapped['Message'] = relationship(back_populates='attachments')
    