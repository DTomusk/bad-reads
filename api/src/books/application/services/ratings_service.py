from abc import ABC, abstractmethod
from uuid import UUID, uuid4

from src.books.domain.models import Rating, RatingScore
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.infrastructure.api.models import Failure, Outcome


class AbstractRatingsService(ABC):
    @abstractmethod
    def create_rating(self, book_id: str, user_id: str, love_score: int, shit_score: int) -> Outcome[UUID]:
        """
        A number of things have to happen every time a rating is created
        The Rating itself has to be created, the book's average has to be updated, and the global average has to be updated
        """
        pass

class RatingsService(AbstractRatingsService):
    def __init__(
        self, 
        rating_repository: AbstractRatingRepo, 
        book_repository: AbstractBookRepo):
        self.rating_repository = rating_repository
        self.book_repository = book_repository

    def create_rating(self, book_id, user_id, love_score, shit_score):
        # Check if the book exists
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            return Outcome(isSuccess=False, failure=Failure(error="Book not found"))

        # Check if the user has already rated the book
        existing_rating = self.rating_repository.get_rating_by_user_and_book(user_id, book_id)
        if existing_rating:
            return Outcome(isSuccess=False, failure=Failure(error="You've already rated this book"))
        
        new_rating = Rating(uuid4(), book.id, user_id, RatingScore(love_score), RatingScore(shit_score))
        self.rating_repository.create_rating(new_rating)
        book.add_rating(new_rating)
        self.book_repository.update_book(book)

        return Outcome(isSuccess=True, data=new_rating.id)