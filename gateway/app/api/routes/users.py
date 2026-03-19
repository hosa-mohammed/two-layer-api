from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.service_client import forward_user_to_service

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    return forward_user_to_service(user.model_dump())