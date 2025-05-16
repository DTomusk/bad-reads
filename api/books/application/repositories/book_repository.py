from abc import ABC, abstractmethod

from sqlalchemy import UUID

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
    def get_books(self, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get all books.
        :param page: The page number to retrieve.
        :param page_size: The number of books per page.
        :param sort_by: The field to sort the books by.
        :param sort_order: The order to sort the books by.
        :return: A list of book objects.
        """
        pass

    @abstractmethod
    def get_books_by_author(self, author_id: UUID, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get books by author.
        :param author_id: The ID of the author to retrieve books for.
        :param page: The page number to retrieve.
        :param page_size: The number of books per page.
        :param sort_by: The field to sort the books by.
        :param sort_order: The order to sort the books by.
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
