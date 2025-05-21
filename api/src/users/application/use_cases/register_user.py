from uuid import uuid4
from src.users.application.repositories.user_repository import UserRepository
from src.users.application.utilities.hasher import Hasher
from src.users.domain.models import Email, User

class RegisterUser:
    def __init__(self, user_repository: UserRepository, hasher: Hasher):
        self.user_repository = user_repository
        self.hasher = hasher

    def execute(self, email: str, password: str) -> User:
        # No point calling the repository if the email is invalid
        user_email = Email(email=email)
        existing_user = self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("User already exists with this email.")
        id = uuid4()
        hashed_password = self.hasher.hash(password)
        user = User(id=id, email=user_email, hashed_password=hashed_password)
        self.user_repository.save(user)
        return user
