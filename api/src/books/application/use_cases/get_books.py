from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.domain.models import Book

# Note: this is a generic use case to get books
# We'll want to have different use cases e.g. for popular books, new books, bad books, etc.
class GetBooks:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(
            self, 
            page: int = 1, 
            page_size: int = 10, 
            sort_by: str = "title", 
            sort_order: str = "asc",
            author_id: str = None,
        ) -> list[Book]:
        if author_id:
            return self.book_repository.get_books_by_author(author_id, page, page_size, sort_by, sort_order)
        return self.book_repository.get_books(page, page_size, sort_by, sort_order)