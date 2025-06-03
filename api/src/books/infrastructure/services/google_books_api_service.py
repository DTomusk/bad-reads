import uuid
import httpx
from src.books.application.repositories.author_repository import AbstractAuthorRepo
from src.books.application.services.external_books_service import AbstractBooksService
from src.books.domain.models import Book, Author, ISBN13


class GoogleBooksApiService(AbstractBooksService):
    def __init__(self, author_repo: AbstractAuthorRepo):
        self.author_repo = author_repo

    def search_books(self, query: str, page_size: int = 10) -> list[Book]:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={page_size}"
        response = httpx.get(url)
        response.raise_for_status()
        books_data = response.json().get("items", [])

        books = []

        for book_data in books_data:
            volume_info = book_data.get("volumeInfo", {})
            
            # Get ISBN-13 from industry identifiers
            isbn = None
            for identifier in volume_info.get("industryIdentifiers", []):
                if identifier.get("type") == "ISBN_13":
                    try:
                        isbn = ISBN13(identifier.get("identifier"))
                        break
                    except ValueError:
                        continue

            if isbn is None:
                continue

            # Don't add books without authors to the database
            if not volume_info.get("authors") or len(volume_info.get("authors")) == 0:
                continue

            # Create Author objects from author names
            # TODO: check repo if author exists, if not, create new author
            # otherwise we can get duplicates
            authors = []
            for author_name in volume_info.get("authors", []):
                author = self.author_repo.get_author_by_name(author_name)
                if author is None:
                    author = Author(id=uuid.uuid4(), name=author_name)
                    self.author_repo.add_author(author)
                authors.append(author)
                
            book = Book(
                id=uuid.uuid4(),
                title=volume_info.get("title", ""),
                authors=authors,
                average_rating=0.0,
                number_of_ratings=0.0,
                sum_of_ratings=0.0,
                isbn=isbn,
                description=volume_info.get("description"),
            )
            books.append(book)

        return books
