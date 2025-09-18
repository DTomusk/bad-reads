from abc import ABC, abstractmethod

from sqlalchemy import UUID
from sqlalchemy.orm import Session

from src.books.domain.models import Rating, RatingScore
from src.books.application.models import GlobalRatingStatsModel, RatingModel

class AbstractRatingRepo(ABC):
    @abstractmethod
    def get_rating_by_user_and_book(self, user_id: UUID, book_id: UUID) -> Rating:
        """
        Get a rating by user and book.
        :param user_id: The ID of the user who rated the book.
        :param book_id: The ID of the book that was rated.
        :return: The rating object.
        """
        pass

    @abstractmethod
    def get_ratings_by_book_id(self, book_id: UUID) -> list[Rating]:
        """
        Get all ratings for a book.
        :param book_id: The ID of the book to get ratings for.
        :return: A list of rating objects.
        """
        pass

    @abstractmethod
    def get_rating_by_id(self, rating_id: UUID) -> Rating:
        """
        Gets the rating with the given ID
        :param rating_id: The ID of the rating 
        :return: A Rating, will return None if it doesn't exist
        """
        pass

    @abstractmethod
    def create_rating(rating: Rating) -> None:
        """
        Create a new rating in the repository.
        :param rating: The rating object to create.
        :return: None
        """
        pass

    @abstractmethod
    def update_rating(rating: Rating) -> None:
        """
        Update a rating in the repository.
        :param rating: The rating object to update.
        :return: None
        """
        pass

    @abstractmethod
    def get_global_stats() -> GlobalRatingStatsModel:
        """
        Gets the global stats entry
        :return: The global stats entry, including average ratings
        """

    @abstractmethod
    def add_rating_to_global_stats(rating: Rating) -> None:
        """
        Update global rating stats with new rating
        :param rating: The rating needed to be added to the global stats
        :return: None
        """
        pass

    @abstractmethod
    def update_rating_in_global_stats(self, old_rating: Rating, new_rating: Rating) -> None:
        """
        Update global rating stats with an updated rating
        """
        pass

class RatingRepo(AbstractRatingRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_rating_by_user_and_book(self, user_id: UUID, book_id: UUID) -> Rating:
        result = (self.session.query(RatingModel)
            .filter(RatingModel.user_id == user_id, RatingModel.book_id == book_id)
            .first()
        )
        if not result:
            return None
        return Rating(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            love_score=RatingScore(result.love_score),
            shit_score=RatingScore(result.shit_score)
        )
    
    def get_ratings_by_book_id(self, book_id: UUID) -> list[Rating]:
        result = self.session.query(RatingModel).filter(RatingModel.book_id == book_id).all()
        return [Rating(
            id=result.id, 
            book_id=result.book_id, 
            user_id=result.user_id, 
            love_score=RatingScore(result.love_score),
            shit_score=RatingScore(result.shit_score)
            ) 
            for result in result]
    
    def get_rating_by_id(self, rating_id) -> Rating:
        result = self.session.query(RatingModel).filter(RatingModel.id == rating_id).first()
        if not result:
            return None
        return Rating(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            love_score=RatingScore(result.love_score),
            shit_score=RatingScore(result.shit_score)
        ) 

    def create_rating(self, rating: Rating):
        rating_model = RatingModel(
            id=rating.id,
            book_id=rating.book_id,
            user_id=rating.user_id,
            love_score=rating.love_score.value,
            shit_score=rating.shit_score.value,
        )
        self.session.add(rating_model)
        self.session.commit()

    def update_rating(self, rating: Rating):
        rating_model = self.session.query(RatingModel).filter(RatingModel.id == rating.id).first()
        if rating_model:
            rating_model.love_score = rating.love_score.value
            rating_model.shit_score = rating.shit_score.value
            self.session.commit()
        else:
            raise ValueError("Rating not found")
        
    def add_rating_to_global_stats(self, rating: Rating):
        global_stats = self.session.query(GlobalRatingStatsModel).first()
        # TODO: this should be logged 
        if global_stats is None:
            return
        
        global_stats.num_ratings += 1

        global_stats.sum_love_ratings += rating.love_score.value
        global_stats.mean_love_rating = global_stats.sum_love_ratings / global_stats.num_ratings

        global_stats.sum_shit_ratings += rating.shit_score.value
        global_stats.mean_shit_rating = global_stats.sum_shit_ratings / global_stats.num_ratings

        self.session.commit()

    def update_rating_in_global_stats(self, old_rating: Rating, new_rating: Rating):
        global_stats = self.session.query(GlobalRatingStatsModel).first()
        # TODO: this should be logged 
        if global_stats is None:
            return
        
        love_delta = new_rating.love_score.value - old_rating.love_score.value
        shit_delta = new_rating.shit_score.value - old_rating.shit_score.value

        global_stats.sum_love_ratings += love_delta
        global_stats.mean_love_rating = global_stats.sum_love_ratings / global_stats.num_ratings
        global_stats.sum_shit_ratings += shit_delta
        global_stats.mean_shit_rating = global_stats.sum_shit_ratings / global_stats.num_ratings

        self.session.commit()

    def get_global_stats(self) -> GlobalRatingStatsModel:
        return self.session.query(GlobalRatingStatsModel).first()
