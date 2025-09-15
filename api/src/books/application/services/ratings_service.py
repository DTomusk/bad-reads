from abc import ABC, abstractmethod
from typing import Tuple
from uuid import UUID, uuid4

from src.books.application.models import GlobalRatingStatsModel
from src.infrastructure.services.background_task_queue import BackgroundTaskQueue
from src.books.domain.models import Book, Rating, RatingScore
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
            book_repository: AbstractBookRepo,
            background_task_queue: BackgroundTaskQueue
        ):
        self.rating_repository = rating_repository
        self.book_repository = book_repository
        self.background_task_queue = background_task_queue

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

        # Updating values on the book itself and the global data shouldn't be blocking
        self.background_task_queue.add_task(self._update_ratings, book, new_rating)

        print("Created rating")
        return Outcome(isSuccess=True, data=new_rating.id)
    
    def _update_ratings(self, book: Book, rating: Rating):
        print("Running rating side effects")
        book.add_rating(rating)
        weighted_love_rating, weighted_shit_rating = self._calculate_weighted_ratings(book)
        self.book_repository.update_book(book, weighted_love_rating, weighted_shit_rating)
        self.rating_repository.add_rating_to_global_stats(rating)

    def _calculate_weighted_ratings(self, book: Book) -> Tuple[float, float]:
        global_stats: GlobalRatingStatsModel = self.rating_repository.get_global_stats()
        weighted_love = self._calculate_single_weighted_rating(book.average_love_rating, book.number_of_ratings, global_stats.mean_love_rating)
        weighted_shit = self._calculate_single_weighted_rating(book.average_shit_rating, book.number_of_ratings, global_stats.mean_shit_rating)
        return (weighted_love, weighted_shit)

    def _calculate_single_weighted_rating(self, average_score: float, num_ratings: int, global_average: float) -> float:
        tuning_param = 1
        rating_part = (num_ratings / (num_ratings + tuning_param)) * average_score
        global_part = (tuning_param / (num_ratings + tuning_param)) * global_average
        return rating_part + global_part