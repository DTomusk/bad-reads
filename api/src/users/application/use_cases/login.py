from src.infrastructure.api.models import Failure, Outcome
from src.users.application.repositories.user_repository import AbstractUserRepository
from src.users.application.utilities.hasher import Hasher
from src.users.application.utilities.token_service import TokenService


class Login:
    def __init__(self, user_repository: AbstractUserRepository, hasher: Hasher, token_service: TokenService):
        self.user_repository = user_repository
        self.hasher = hasher
        self.token_service = token_service

    def execute(self, email: str, password: str) -> Outcome[str]:
        user = self.user_repository.get_by_email(email)
        if not user or not self.hasher.verify(password, user.hashed_password):
            return Outcome(isSuccess=False, failure=Failure(error="Invalid credentials."))
        
        token = self.token_service.create_token(
            data={
                "sub": str(user.id),
                "username": user.username.username
            }, expires_minutes=30)
        return Outcome[str](isSuccess=True, data=token)
        
