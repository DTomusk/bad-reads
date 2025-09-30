from abc import ABC, abstractmethod

import uuid
import httpx
from ...data.author_repository import AbstractAuthorRepo
from ...domain.models import Book, Author

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

class GoogleBooksApiService(AbstractBooksService):
    def __init__(self, author_repo: AbstractAuthorRepo):
        self.author_repo = author_repo

    def search_books(self, query: str, page_size: int = 10, start_index: int = 0) -> list[Book]:
        books = []

        if page_size == 0:
            return books
        
        books_data = self._get_books_data(query, page_size, start_index)

        for book_data in books_data:
            volume_info = book_data.get("volumeInfo", {})

            # Don't add books without authors to the database
            if not volume_info.get("authors") or len(volume_info.get("authors")) == 0:
                continue

            # Don't add books that are not in English
            # TODO: add support for other languages
            if not volume_info.get("language") == "en":
                continue

            # Create Author objects from author names
            authors = self._get_authors(volume_info.get("authors", []))

            book = self._create_book(volume_info, authors)

            books.append(book)

        return books

    def _get_books_data(self, query: str, page_size: int, start_index: int) -> list[dict]:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={page_size}&startIndex={start_index}"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json().get("items", [])

    def _get_authors(self, author_names: list[str]) -> list[Author]:
        authors = []
        for author_name in author_names:
            author = self.author_repo.get_author_by_name(author_name)
            if author is None:
                author = Author(id=uuid.uuid4(), name=author_name)
                self.author_repo.add_author(author)
            authors.append(author)
        return authors

    def _create_book(self, volume_info: dict, authors: list[Author]) -> Book:
        return Book(
            id=uuid.uuid4(),
            title=volume_info.get("title", ""),
            authors=authors,
            average_love_rating=0.0,
            average_shit_rating=0.0,
            number_of_ratings=0,
            sum_of_love_ratings=0.0,
            sum_of_shit_ratings=0.0,
            description=volume_info.get("description"),
            picture_url=volume_info.get("imageLinks", {}).get("thumbnail")
        )
