from fastapi import APIRouter
from app.api.v1.users import users_router
from app.api.v1.messages import messages_router
from app.api.v1.dialogues import dialogues_router
from app.api.v1.dialogue_participants import participants_router


v1_router = APIRouter(prefix="/v1")
v1_router.include_router(users_router, tags=["Users"])
v1_router.include_router(messages_router, tags=["Messages"])
v1_router.include_router(dialogues_router, tags=["Dialogues"])
v1_router.include_router(participants_router, tags=["Participants"])

