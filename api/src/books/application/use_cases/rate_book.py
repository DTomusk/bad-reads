from uuid import UUID, uuid4

from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.books.domain.models import Book, Rating, RatingScore, Review


class RateBook:
    def __init__(self, book_repository: AbstractBookRepo, rating_repository: AbstractRatingRepo):
        self.book_repository = book_repository
        self.rating_repository = rating_repository

    def execute(self, book_id: UUID, user_id: UUID, love_score: float, shit_score: float) -> Book:
        """ User rates a book """
        # Check if the book exists
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        # Check if the user has already rated the book
        existing_rating = self.rating_repository.get_rating_by_user_and_book(user_id, book_id)
        if existing_rating:
            raise ValueError("Book already rated by user")
        else:
            new_rating = Rating(uuid4(), book_id, user_id, RatingScore(love_score), RatingScore(shit_score))
            self.rating_repository.create_rating(new_rating)
            book.add_rating(new_rating)
            self.book_repository.update_book(book)
        return book