from uuid import UUID

from sqlalchemy.orm import Session

from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.domain.models import Review, Rating, RatingScore 
from src.books.infrastructure.models import ReviewModel, RatingModel
from src.books.api.schemas.review_response import ReviewResponse


class ReviewRepo(AbstractReviewRepo):
    def __init__(self, session: Session):
        self.session = session

    def create_review(self, review: Review) -> None:
        review_model = ReviewModel(
            id=review.id,
            book_id=review.book_id,
            user_id=review.user_id,
            text=review.text,
            rating_id=review.rating_id,
            date_created=review.date_created
        )
        self.session.add(review_model)
        self.session.commit()

    def _create_review_response(self, review_model: ReviewModel) -> ReviewResponse:
        rating_model = self.session.query(RatingModel).filter(RatingModel.id == review_model.rating_id).first()
        if not rating_model:
            return None
            
        review = Review(
            id=review_model.id,
            book_id=review_model.book_id,
            user_id=review_model.user_id,
            text=review_model.text,
            rating_id=review_model.rating_id,
            date_created=review_model.date_created
        )
        rating = Rating(
            book_id=review_model.book_id,
            user_id=review_model.user_id,
            id=rating_model.id,
            love_score=RatingScore(rating_model.love_score),
            shit_score=RatingScore(rating_model.shit_score)
        )
        return ReviewResponse.from_domain(review, rating)

    def get_reviews_by_book_id(self, book_id: UUID, sort_by: str = "date_created", sort_order: str = "desc", limit: int = 10) -> list[ReviewResponse]:
        result = (self.session.query(ReviewModel)
            .filter(ReviewModel.book_id == book_id)
            .order_by(getattr(ReviewModel, sort_by).asc() if sort_order == "asc" else getattr(ReviewModel, sort_by).desc())
            .limit(limit)
            .all())
        if not result:
            return []
        
        review_responses = []
        for review_model in result:
            review_response = self._create_review_response(review_model)
            if review_response:
                review_responses.append(review_response)
        
        return review_responses

    def get_reviews_by_user_id(self, user_id: UUID) -> list[ReviewResponse]:
        result = self.session.query(ReviewModel).filter(ReviewModel.user_id == user_id).all()
        if not result:
            return []
        
        review_responses = []
        for review_model in result:
            review_response = self._create_review_response(review_model)
            if review_response:
                review_responses.append(review_response)
        
        return review_responses

    def get_review_by_id(self, review_id: UUID) -> ReviewResponse:
        result = self.session.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if not result:
            return None
        return self._create_review_response(result)
    
    def get_review_by_user_and_book(self, user_id: UUID, book_id: UUID) -> ReviewResponse:
        result = self.session.query(ReviewModel).filter(
            ReviewModel.user_id == user_id, 
            ReviewModel.book_id == book_id
        ).first()
        if not result:
            return None
        return self._create_review_response(result)
    
