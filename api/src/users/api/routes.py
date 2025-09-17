from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.shared.api.dependencies import get_profanity_service
from src.infrastructure.api.models import Outcome
from src.users.api.dependencies import get_login_use_case, get_register_user_use_case
from src.users.api.schemas.registration_request import RegistrationRequest

router = APIRouter()

@router.post("/register")
async def register_user(registration_request: RegistrationRequest, register_user_use_case=Depends(get_register_user_use_case)):
    """Register a new user."""
    outcome: Outcome = register_user_use_case.execute(
        email=registration_request.email, 
        password=registration_request.password,
        username=registration_request.username
    )

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)
    
    user = outcome.data

    return {"id": str(user.id), "email": user.email.email}

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm=Depends(), login_use_case=Depends(get_login_use_case)):
    """Login a user and return a JWT token."""
    email = form_data.username
    password = form_data.password
    outcome: Outcome = login_use_case.execute(email=email, password=password)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)
    
    token = outcome.data

    return {"access_token": token, "token_type": "Bearer"}