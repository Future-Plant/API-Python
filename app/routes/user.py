from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserLogin
from app.services.auth_service import signup_user, login_user

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/signup")
def signup(user: UserCreate):
    return signup_user(user)

@router.post("/login")
def login(user: UserLogin):
    return login_user(user)
