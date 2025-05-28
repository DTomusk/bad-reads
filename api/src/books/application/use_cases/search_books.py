from api.src.books.domain.models import Book
from src.books.application.repositories.book_repository import AbstractBookRepo

class SearchBooks:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(
            self, 
            query: str,
            page: int = 1,
            page_size: int = 10,
            sort_by: str = "title",
            sort_order: str = "asc",
        ) -> list[Book]:
        # Note: this grabs all books in the database and does a fuzzy search on the title in memory
        # TODO: we should use a more efficient search method e.g. a database index
        db_books = self.book_repository.search_books(page, page_size, sort_by, sort_order)
