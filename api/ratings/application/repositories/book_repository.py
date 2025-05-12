from abc import ABC, abstractmethod

from api.ratings.domain.models import Book


class BookRepo(ABC):
    @abstractmethod
    def get_book_by_id(self, book_id: str) -> Book:
        """
        Get a book by its ID.
        :param book_id: The ID of the book to retrieve.
        :return: The book object.
        """
        pass