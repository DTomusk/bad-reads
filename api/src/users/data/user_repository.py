from abc import ABC, abstractmethod
from typing import Optional

from uuid import UUID
from sqlalchemy.orm import Session

from ..domain.models import Email, User, Username
from .models import UserModel

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username."""
        pass

    @abstractmethod
    def get_by_ids(self, user_ids: list[UUID]) -> dict[str, User]:
        """
        Get a list of users by a list of ids
        """
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user."""
        pass

class UserRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_email(self, email: str) -> Optional[User]:
        result = self.session.query(UserModel).filter_by(email=email).first()
        if result: 
            return User(
                id=result.id,
                email=Email(result.email),
                hashed_password=result.hashed_password,
                username=Username(result.username),
            )
        return None
    
    def get_by_username(self, username: str) -> Optional[User]:
        result = self.session.query(UserModel).filter_by(username=username).first()
        if result: 
            return User(
                id=result.id,
                email=Email(result.email),
                hashed_password=result.hashed_password,
                username=Username(result.username),
            )
        return None
    
    def get_by_ids(self, user_ids):
        results = self.session.query(UserModel).filter(UserModel.id.in_(user_ids)).all()
        users_by_id = {
            row.id: User(
                id=row.id,
                email=Email(row.email),
                hashed_password=row.hashed_password,
                username=Username(row.username),
            )
            for row in results
        }
        return users_by_id
    
    def save(self, user: User):
        db_user = UserModel(
            id=user.id,
            email=user.email.email,
            hashed_password=user.hashed_password,
            username=user.username.username,
        )
        self.session.add(db_user)
        self.session.commit()