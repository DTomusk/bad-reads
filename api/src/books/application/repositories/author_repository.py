from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.books.domain.models import Author

class AbstractAuthorRepo(ABC):
    @abstractmethod
    def get_author_by_id(self, author_id: UUID) -> Author:
        pass

    @abstractmethod
    def get_author_by_name(self, name: str) -> Author:
        pass

    @abstractmethod
    def add_author(self, author: Author) -> Author:
        pass
    
    
