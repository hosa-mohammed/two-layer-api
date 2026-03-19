from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user_service import create_user

router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)