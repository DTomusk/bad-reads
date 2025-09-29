from pydantic import BaseModel
from src.books.api.schemas.responses.book_response import BookResponse
from src.books.domain.models import Book

class BookSearchResponse(BaseModel):
    books: list[BookResponse]
    has_more: bool

    @classmethod
    def from_domain(cls, books: list[Book], has_more: bool) -> "BookSearchResponse":
        return cls(books=[BookResponse.from_domain(book) for book in books], has_more=has_more)