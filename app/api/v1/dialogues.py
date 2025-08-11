from fastapi import APIRouter
from typing import List

from app.schemas.dialogue import DialogueResponse, DialogueCreate 


dialogues_router = APIRouter(prefix="/dialogues")

@dialogues_router.get('/', summary="Получить список диалогов", response_model=List[DialogueResponse])
async def list_dialogues():
    pass


@dialogues_router.post('/create', summary="Создать диалог", response_model=DialogueCreate)
async def create_dialogue():
    pass


@dialogues_router.get('/{dialogue_id}', summary="Получить данные о диалоге", response_model=DialogueResponse)
async def get_dialogue ():
    pass
