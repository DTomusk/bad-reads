from uuid import uuid4
from src.infrastructure.api.models import Failure, Outcome
from src.users.application.repositories.user_repository import AbstractUserRepository
from src.users.application.utilities.hasher import Hasher
from src.users.domain.models import Email, User, Username


class RegisterUser:
    def __init__(self, user_repository: AbstractUserRepository, hasher: Hasher):
        self.user_repository = user_repository
        self.hasher = hasher

    def execute(self, email: str, password: str, username: str) -> Outcome[User]:
        email_outcome = self._validate_and_check_email(email)
        if not email_outcome.isSuccess:
            return email_outcome
        user_email = email_outcome.data

        username_outcome = self._validate_and_check_username(username)
        if not username_outcome.isSuccess:
            return username_outcome
        user_username = username_outcome.data

        user = User(
            id=uuid4(),
            email=user_email,
            hashed_password=self.hasher.hash(password),
            username=user_username,
        )

        try:
            self.user_repository.save(user)
        except Exception:
            return Outcome[User](
                isSuccess=False,
                failure=Failure(error="Failed to save user to repository.", code=500),
            )

        return Outcome[User](isSuccess=True, data=user)

    def _validate_and_check_email(self, email: str) -> Outcome[Email]:
        try:
            user_email = Email(email=email)
        except ValueError as ve:
            return Outcome[Email](isSuccess=False, failure=Failure(error=str(ve), code=400))

        if self.user_repository.get_by_email(email):
            return Outcome[Email](isSuccess=False, failure=Failure(error="Email already in use.", code=400))

        return Outcome[Email](isSuccess=True, data=user_email)

    def _validate_and_check_username(self, username: str) -> Outcome[Username]:
        try:
            user_username = Username(username=username)
        except ValueError as ve:
            return Outcome[Username](isSuccess=False, failure=Failure(error=str(ve), code=400))

        if self.user_repository.get_by_username(username):
            return Outcome[Username](isSuccess=False, failure=Failure(error="Username already in use.", code=400))

        return Outcome[Username](isSuccess=True, data=user_username)
