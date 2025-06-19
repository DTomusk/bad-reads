from src.books.application.services.external_books_service import AbstractBooksService
from src.books.domain.models import Book
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.author_repository import AbstractAuthorRepo
from src.infrastructure.services.background_task_queue import BackgroundTaskQueue

class SearchBooks:
    def __init__(self, book_repository: AbstractBookRepo, external_books_service: AbstractBooksService, author_repository: AbstractAuthorRepo, background_task_queue: BackgroundTaskQueue):
        self.book_repository = book_repository
        self.external_books_service = external_books_service
        self.author_repository = author_repository
        self.background_task_queue = background_task_queue

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
                    self.background_task_queue.add_task(self.author_repository.add_author, author)  
            existing_book = self.book_repository.get_book_by_isbn(external_book.isbn)
            if not existing_book:
                self.background_task_queue.add_task(self.book_repository.add_book, external_book)

    def execute(
            self, 
            query: str,
            page_size: int = 10,
        ) -> list[Book]:
        # TODO: figure out pagination 
        if not query:
            return []
            
        db_books = self.book_repository.search_books(query, page_size)
        
        # Queue the external book search and processing as a background task
        self.background_task_queue.add_task(self._process_external_books, query, page_size)
        
        return db_books

