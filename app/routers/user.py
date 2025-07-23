from fastapi import APIRouter
from app.models.user import UserCreate, User
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user_route(user: UserCreate):
     return create_user(user)