from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy.orm import Session, joinedload

from ..application.models import ReviewWithBookDetailsDTO, RatingWithReviewDTO

from .models import BookModel, RatingModel, ReviewModel


class AbstractRatingWithReviewReader(ABC):
    @abstractmethod
    def get_rating_with_review_for_user_and_book(self, user_id: UUID, book_id: UUID) -> RatingWithReviewDTO:
        """
        Get the user's rating and review for a book (if it exists)
        """
        pass

    @abstractmethod
    def get_reviews_with_ratings_for_user(self, user_id: UUID) -> list[ReviewWithBookDetailsDTO]:
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
            return _get_dto_from_rating(rating)
        
        return _get_dto_from_models(rating, review)
    
    def get_reviews_with_ratings_for_user(self, user_id) -> list[ReviewWithBookDetailsDTO]:
        results = (
            self.session.query(ReviewModel)
            .filter(ReviewModel.user_id == user_id)
            .options(
                    joinedload(ReviewModel.rating), 
                    joinedload(ReviewModel.book)
                )
            .all()
        )

        dtos: list[ReviewWithBookDetailsDTO] = []

        for review in results: 
            dtos.append(ReviewWithBookDetailsDTO(
                love_score=review.rating.love_score,
                shit_score=review.rating.shit_score,
                text=review.text,
                book_id=review.book_id,
                picture_url=review.book.picture_url,
                title=review.book.title
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
            dtos.append(_get_dto_from_models(rating, review))

        return dtos
    
def _get_dto_from_rating(rating: RatingModel):
    return RatingWithReviewDTO(
        book_id=rating.book_id,
        user_id=rating.user_id,
        love_score=rating.love_score,
        shit_score=rating.shit_score,
        date_created=None,
        text=None
    )

def _get_dto_from_models(rating: RatingModel, review: ReviewModel):
    return RatingWithReviewDTO(
        book_id=rating.book_id,
        user_id=rating.user_id,
        love_score=rating.love_score,
        shit_score=rating.shit_score,
        date_created=review.date_created,
        text=review.text
    )
