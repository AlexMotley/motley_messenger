from fastapi import APIRouter
from typing import List

from app.schemas.dialogue_participants import DialogueParticipantResponse, DialogueParticipantCreate


participants_router = APIRouter(prefix="/participants")

@participants_router.get('/dialogue/{dialogue_id}', summary="Получить список участников диалога", response_model=List[DialogueParticipantResponse])
async def get_participants_from_dialogue():
    pass


@participants_router.post('/attach', summary="Записать участников диалога", response_model=DialogueParticipantCreate)
async def create_participants():
    pass
