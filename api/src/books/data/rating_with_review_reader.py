from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy.orm import Session

from .models import RatingModel, ReviewModel

from ..application.models.rating_with_review_dto import RatingWithReviewDTO


class AbstractRatingWithReviewReader(ABC):
    @abstractmethod
    def get_rating_with_review_for_user_and_book(self, user_id: UUID, book_id: UUID) -> RatingWithReviewDTO:
        """
        Get the user's rating and review for a book (if it exists)
        """
        pass

    @abstractmethod
    def get_reviews_with_ratings_for_user(self, user_id: UUID) -> list[RatingWithReviewDTO]:
        """
        Get all the user's reviews and their corresponding ratings
        """
        pass

    @abstractmethod
    def get_reviews_with_ratings_for_book(self, book_id: UUID) -> list[RatingWithReviewDTO]:
        """
        Get all reviews with ratings for a book
        """
        pass

class RatingWithReviewReader(AbstractRatingWithReviewReader):
    def __init__(self, session: Session):
        self.session = session

    def get_rating_with_review_for_user_and_book(self, user_id, book_id):
        rating, review = (self.session.query(RatingModel, ReviewModel)
            .join(ReviewModel, RatingModel.id == ReviewModel.rating_id)
            .filter(
                RatingModel.book_id == book_id,
                RatingModel.user_id == user_id
            )
            .first())
        
        if not rating: 
            return None
        
        if not review:
            return RatingWithReviewDTO(
                love_score=rating.love_score,
                shit_score=rating.shit_score,
                text=None)
        
        return RatingWithReviewDTO(
                love_score=rating.love_score,
                shit_score=rating.shit_score,
                text=review.text)
    
    def get_reviews_with_ratings_for_user(self, user_id):
        results = (
            self.session.query(RatingModel, ReviewModel)
            .join(ReviewModel, RatingModel.id == ReviewModel.rating_id)
            .filter(RatingModel.user_id == user_id)
            .all()
        )

        dtos: list[RatingWithReviewDTO] = []

        for rating, review in results: 
            dtos.append(RatingWithReviewDTO(
                love_score=rating.love_score,
                shit_score=rating.shit_score,
                text=review.text
            ))

        return dtos
    
    def get_reviews_with_ratings_for_book(self, book_id):
        results = (
            self.session.query(RatingModel, ReviewModel)
            .join(ReviewModel, RatingModel.id == ReviewModel.rating_id)
            .filter(RatingModel.book_id == book_id)
            .all()
        )

        dtos: list[RatingWithReviewDTO] = []

        for rating, review in results: 
            dtos.append(RatingWithReviewDTO(
                love_score=rating.love_score,
                shit_score=rating.shit_score,
                text=review.text
            ))

        return dtos
