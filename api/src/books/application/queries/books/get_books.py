from src.books.api.schemas.book_sort_options import BookSortOption
from ....data.book_repository import AbstractBookRepo
from ....domain.models import Book

class GetBooks:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(
            self, 
            page: int = 1, 
            page_size: int = 10, 
            sort_by: BookSortOption = BookSortOption.alphabetical, 
            sort_order: str = "asc",
        ) -> list[Book]:
        if sort_by == BookSortOption.alphabetical:
            return self.book_repository.get_books_alphabetically(page, page_size, sort_order)
        if sort_by == BookSortOption.most_loved:
            return self.book_repository.get_books_by_hearts(page, page_size, sort_order)
        if sort_by == BookSortOption.most_poos:
            return self.book_repository.get_books_by_poos(page, page_size, sort_order)
        return []