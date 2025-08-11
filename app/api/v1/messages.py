from fastapi import APIRouter
from typing import List

from app.schemas.message import MessageResponse, MessageCreate


messages_router = APIRouter(prefix="/messages")

@messages_router.get('/{message_id}', summary="Получить данные о сообщении", response_model=MessageResponse)
async def get_message():
    pass


@messages_router.post('/create', summary="Создать сообщение", response_model=MessageCreate)
async def create_message():
    pass

