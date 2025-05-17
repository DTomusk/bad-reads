from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.users.api.dependencies import get_login_use_case, get_register_user_use_case
from api.users.api.schemas.registration_request import RegistrationRequest

router = APIRouter()

@router.post("/register")
async def register_user(registration_request: RegistrationRequest, register_user_use_case=Depends(get_register_user_use_case)):
    """Register a new user."""
    user = register_user_use_case.execute(email=registration_request.email, password=registration_request.password)
    return {"id": str(user.id), "email": user.email.email}

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm=Depends(), login_use_case=Depends(get_login_use_case)):
    """Login a user and return a JWT token."""
    email = form_data.username
    password = form_data.password
    token = login_use_case.execute(email=email, password=password)
    return {"access_token": token, "token_type": "Bearer"}