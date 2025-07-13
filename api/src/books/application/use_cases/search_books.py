from src.books.application.services.external_books_service import AbstractBooksService
from src.books.domain.models import Book
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.author_repository import AbstractAuthorRepo
from src.books.api.schemas.book_search_response import BookSearchResponse

class SearchBooks:
    def __init__(self, book_repository: AbstractBookRepo, external_books_service: AbstractBooksService, author_repository: AbstractAuthorRepo):
        self.book_repository = book_repository
        self.external_books_service = external_books_service
        self.author_repository = author_repository

    def _process_external_books(self, query: str, page_size: int):
        external_books = self.external_books_service.search_books(query, page_size=page_size)
        
        # Search for books that are not in the database and add them to the database
        for external_book in external_books:
            # Don't add books without authors to the database
            if not external_book.authors:
                continue
            for author in external_book.authors:
                existing_author = self.author_repository.get_author_by_name(author.name)
                if not existing_author:
                    existing_author = self.author_repository.add_author(author)  
            existing_book = self.book_repository.get_book_by_title_and_author(external_book.title, existing_author.name)
            if not existing_book:
                self.book_repository.add_book(external_book)

    def execute(
            self, 
            query: str,
            page_size: int = 10,
            page: int = 1
        ) -> BookSearchResponse:
        if not query:
            return BookSearchResponse(books=[], has_more=False)
        
        if page < 1:
            return BookSearchResponse(books=[], has_more=False)
        
        # For simplicity, just search db for the next page, don't bother with external api
        if page > 1:
            db_books = self.book_repository.search_books(query, page_size + 1, page)
            has_more = len(db_books) == page_size + 1
            # Only return up to page_size books
            books_to_return = db_books[:page_size]
            return BookSearchResponse.from_domain(books_to_return, has_more)
            
        # We essentially do 2 searches to get the books 
        # If there are enough books the first time, then happy days 
        # Otherwise, we copy data from the external api into the db and do a second search
        db_books = self.book_repository.search_books(query, page_size + 1)
        external_books_needed = page_size - len(db_books)
        if external_books_needed > 0:
            # Multiply by 2 to account for duplicates
            self._process_external_books(query, external_books_needed * 2)
            db_books = self.book_repository.search_books(query, page_size + 1)
        
        has_more = len(db_books) == page_size + 1
        # Only return up to page_size books
        books_to_return = db_books[:page_size]
        return BookSearchResponse.from_domain(books_to_return, has_more)

