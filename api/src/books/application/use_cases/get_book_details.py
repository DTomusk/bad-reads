from uuid import UUID
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.rating_repository import AbstractRatingRepo


class GetBookDetails:
    def __init__(self, book_repository: AbstractBookRepo, rating_repository: AbstractRatingRepo):
        self.book_repository = book_repository
        self.rating_repository = rating_repository

    def execute(self, book_id: UUID) -> dict:
        """ Get book details by its ID """
        # Get the book details
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Get the ratings for the book
        ratings = self.rating_repository.get_ratings_by_book_id(book_id)

        return {
             "book": book,
             "ratings": ratings,
        }