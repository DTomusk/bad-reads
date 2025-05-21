from uuid import UUID

from sqlalchemy.orm import Session

from src.books.application.repositories.review_repository import ReviewRepo
from src.books.domain.models import Review
from src.books.infrastructure.models import ReviewModel


class SqliteReviewRepo(ReviewRepo):
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

    def get_reviews_by_book_id(self, book_id: UUID) -> list[Review]:
        result = self.session.query(ReviewModel).filter(ReviewModel.book_id == book_id).all()
        if not result:
            return []
        return [Review(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            text=result.text,
            rating_id=result.rating_id,
            date_created=result.date_created
        ) for result in result]

    def get_reviews_by_user_id(self, user_id: UUID) -> list[Review]:
        result = self.session.query(ReviewModel).filter(ReviewModel.user_id == user_id).all()
        if not result:
            return []
        return [Review(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            text=result.text,
            rating_id=result.rating_id,
            date_created=result.date_created
        ) for result in result]

    def get_review_by_id(self, review_id: UUID) -> Review:
        result = self.session.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if not result:
            return None
        return Review(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            text=result.text,
            rating_id=result.rating_id,
            date_created=result.date_created
        )
    
    def get_review_by_user_and_book(self, user_id: UUID, book_id: UUID) -> Review:
        result = self.session.query(ReviewModel).filter(ReviewModel.user_id == user_id, ReviewModel.book_id == book_id).first()
        if not result:
            return None
        return Review(
            id=result.id,
            book_id=result.book_id,
            user_id=result.user_id,
            text=result.text,
            rating_id=result.rating_id,
            date_created=result.date_created
        )
    
