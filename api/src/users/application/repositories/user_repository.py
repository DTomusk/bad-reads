from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from src.users.domain.models import User
from src.users.application.models import UserModel

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user."""
        pass

class UserRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_email(self, email: str):
        result = self.session.query(UserModel).filter_by(email=email).first()
        if result: 
            return User(
                id=result.id,
                email=result.email,
                hashed_password=result.hashed_password,
            )
        return None
    
    def save(self, user: User):
        db_user = UserModel(
            id=user.id,
            email=user.email.email,
            hashed_password=user.hashed_password,
        )
        self.session.add(db_user)
        self.session.commit()