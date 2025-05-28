from abc import ABC, abstractmethod

from src.books.domain.models import Book


class AbstractBooksService(ABC):
    @abstractmethod
    def search_books(self, query: str) -> list[Book]:
        pass

