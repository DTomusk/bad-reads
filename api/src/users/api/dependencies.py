from fastapi import Depends

from ...infrastructure.api.dependencies import get_profanity_service
from ...infrastructure.db.database import get_session
from ..application.commands.login import Login
from ..application.commands.register_user import RegisterUser
from ..data.user_repository import UserRepository
from ..application.utilities.hasher import BCryptHasher
from ..application.utilities.token_service import JWTTokenService


def get_user_repository(session=Depends(get_session)):
    return UserRepository(session=session)

def get_bcrypt_hasher():
    return BCryptHasher()

def get_token_service():
    return JWTTokenService()

def get_register_user_use_case(user_repo=Depends(get_user_repository), hasher=Depends(get_bcrypt_hasher), profanity_service=Depends(get_profanity_service)):
    return RegisterUser(user_repository=user_repo, hasher=hasher, profanity_service=profanity_service)

def get_login_use_case(user_repo=Depends(get_user_repository), hasher=Depends(get_bcrypt_hasher), token_service=Depends(get_token_service)):
    return Login(user_repository=user_repo, hasher=hasher, token_service=token_service)
