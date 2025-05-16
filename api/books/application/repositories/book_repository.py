from abc import ABC, abstractmethod

from api.books.domain.models import Book


class BookRepo(ABC):
    @abstractmethod
    def get_book_by_id(self, book_id: str) -> Book:
        """
        Get a book by its ID.
        :param book_id: The ID of the book to retrieve.
        :return: The book object.
        """
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        """
        Get all books.
        :return: A list of book objects.
        """
        pass

    @abstractmethod
    def update_book(self, book: Book) -> Book:
        """
        Update a book.
        :param book: The book object to update.
        :return: The updated book object.
        """
        pass
