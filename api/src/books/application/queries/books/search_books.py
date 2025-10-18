from ...services.external_books_service import AbstractBooksService
from ....data.book_repository import AbstractBookRepo
from ....data.author_repository import AbstractAuthorRepo
from src.books.api.schemas.responses.book_search_response import BookSearchResponse
from src.infrastructure.services.background_task_queue import BackgroundTaskQueue

class SearchBooks:
    def __init__(
            self, 
            book_repository: AbstractBookRepo, 
            external_books_service: AbstractBooksService, 
            author_repository: AbstractAuthorRepo, 
            background_task_queue: BackgroundTaskQueue
        ):
        self.book_repository = book_repository
        self.external_books_service = external_books_service
        self.author_repository = author_repository
        self.background_task_queue = background_task_queue

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
        
        if page_size < 1:
            return BookSearchResponse(books=[], has_more=False)
        
        # We essentially do 2 searches to get the books 
        # If there are enough books the first time, then happy days 
        # Otherwise, we copy data from the external api into the db and do a second search
        db_books = self.book_repository.search_books(query, page_size, page)
        external_books_needed = page_size - len(db_books)
        if external_books_needed > 0:
            # Multiply by 2 to account for duplicates
            self._process_external_books(query, page_size * 2, page_size * (page - 1))
            db_books = self.book_repository.search_books(query, page_size, page)
        else:
            # Background a task to process the external books
            self.background_task_queue.add_task(self._process_external_books, query, page_size, page_size * (page - 1))

        has_more = len(db_books) == page_size + 1

        # Only return up to page_size books
        books_to_return = db_books[:page_size]
        return BookSearchResponse.from_domain(books_to_return, has_more)
    
    def _process_external_books(self, query: str, page_size: int, start_index: int):
        external_books = self.external_books_service.search_books(query, page_size=page_size, start_index=start_index)
        
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

