from abc import ABC, abstractmethod

from src.books.domain.models import Book


class AbstractBooksService(ABC):
    @abstractmethod
    def search_books(self, query: str, page_size: int, start_index: int) -> list[Book]:
        """
        Search for books by title from an external api.
        :param query: The query to search for.
        :param page_size: The number of books per page.
        :param start_index: The index of the first book to return.
        :return: A list of book objects.
        """
        pass

