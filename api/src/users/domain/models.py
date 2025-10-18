from dataclasses import dataclass
import re
from uuid import UUID

@dataclass(frozen=True)
class Email:
    _EMAIL_PATTERN = r'^(?!.*\.\.)[a-zA-Z0-9](?:[a-zA-Z0-9._%+-]{0,62}[a-zA-Z0-9])?@[a-zA-Z0-9](?:[a-zA-Z0-9.-]{0,62}[a-zA-Z0-9])?\.[a-zA-Z]{2,}$'
    email: str

    def __post_init__(self):
        if not re.match(self._EMAIL_PATTERN, self.email):
            raise ValueError(f"Invalid email format: {self.email}")
        
@dataclass(frozen=True)
class Username:
    _USERNAME_PATTERN = r'^[a-zA-Z0-9_.-]{3,20}$'
    username: str

    def __post_init__(self):
        if not re.match(self._USERNAME_PATTERN, self.username):
            raise ValueError(f"Invalid username format: {self.username}")

class User:
    def __init__(self, id: UUID, email: Email, hashed_password: str, username: Username):
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.username = username