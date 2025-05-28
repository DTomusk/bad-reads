import uuid
import httpx
from src.books.application.services.external_books_service import AbstractBooksService
from src.books.domain.models import Book, Author, ISBN13


class GoogleBooksApiService(AbstractBooksService):
    def __init__(self):
        pass

    def search_books(self, query: str, max_results: int = 10) -> list[Book]:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
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

            # Create Author objects from author names
            authors = []
            for author_name in volume_info.get("authors", []):
                authors.append(Author(id=uuid.uuid4(), name=author_name))

            average_rating = 0.0
            ratings_count = 0
            sum_of_ratings = 0.0

            book = Book(
                id=uuid.uuid4(),
                title=volume_info.get("title", ""),
                authors=authors,
                average_rating=average_rating,
                number_of_ratings=ratings_count,
                sum_of_ratings=sum_of_ratings,
                isbn=isbn,
                description=volume_info.get("description"),
            )
            books.append(book)

        return books
