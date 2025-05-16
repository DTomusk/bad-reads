from fastapi import Depends

from api.infrastructure.db.database import get_session
from api.users.application.use_cases.login import Login
from api.users.application.use_cases.register_user import RegisterUser
from api.users.infrastructure.repositories.sqlite_user_repository import SqliteUserRepository
from api.users.infrastructure.utilities.bcrypt_hasher import BCryptHasher
from api.users.infrastructure.utilities.jwt_token_service import JWTTokenService


def get_user_repository(session=Depends(get_session)):
    return SqliteUserRepository(session=session)

def get_bcrypt_hasher():
    return BCryptHasher()

def get_token_service():
    return JWTTokenService()

def get_register_user_use_case(user_repo=Depends(get_user_repository), hasher=Depends(get_bcrypt_hasher)):
    return RegisterUser(user_repository=user_repo, hasher=hasher)

def get_login_use_case(user_repo=Depends(get_user_repository), hasher=Depends(get_bcrypt_hasher), token_service=Depends(get_token_service)):
    return Login(user_repository=user_repo, hasher=hasher, token_service=token_service)
