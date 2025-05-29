from src.books.application.services.external_books_service import AbstractBooksService
from src.books.domain.models import Book
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.author_repository import AbstractAuthorRepo

class SearchBooks:
    def __init__(self, book_repository: AbstractBookRepo, external_books_service: AbstractBooksService, author_repository: AbstractAuthorRepo):
        self.book_repository = book_repository
        self.external_books_service = external_books_service
        self.author_repository = author_repository

    def execute(
            self, 
            query: str,
            page_size: int = 10,
        ) -> list[Book]:
        # TODO: figure out pagination 
        db_books = self.book_repository.search_books(query, page_size)

        external_books = self.external_books_service.search_books(query, page_size)

        # Search for books that are not in the database and add them to the database
        for external_book in external_books:
            for author in external_book.authors:
                existing_author = self.author_repository.get_author_by_name(author.name)
                if not existing_author:
                    self.author_repository.add_author(author)
            if not self.book_repository.get_book_by_isbn(external_book.isbn):
                self.book_repository.add_book(external_book)

        # TODO: this could give us more than page_size books and it could give us duplicates
        return db_books + external_books

