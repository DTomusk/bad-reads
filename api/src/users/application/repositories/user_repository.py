from abc import ABC, abstractmethod
from typing import Optional

from src.users.domain.models import User

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user."""
        pass