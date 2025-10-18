from abc import ABC
from uuid import UUID
from sqlalchemy.orm import Session, joinedload

from ...books.data.models import ReviewModel
from .models.review_with_username_dto import ReviewWithUsernameDTO

class AbstractReviewWithUsernameReader(ABC):
    def get_reviews_for_book(book_id: UUID, page_size: int, page: int, sort_order: str) -> list[ReviewWithUsernameDTO]:
        """
        
        """
        pass

class ReviewWithUsernameReader(AbstractReviewWithUsernameReader):
    def __init__(self, session: Session):
        self.session = session

    def get_reviews_for_book(self, book_id, page_size, page, sort_order):
        results = (
            self.session.query(ReviewModel)
                .filter(ReviewModel.book_id == book_id)
                .options(
                    joinedload(ReviewModel.rating), 
                    joinedload(ReviewModel.user)
                )
                .order_by(getattr(ReviewModel, "date_created").asc() if sort_order == "newest" else getattr(ReviewModel, "date_created").desc())
                .offset((page - 1) * page_size)
                .limit(page_size)
                .all()
        )

        return [ReviewWithUsernameDTO(
            love_score=review.rating.love_score,
            shit_score=review.rating.shit_score,
            text=review.text,
            date_created=review.date_created,
            username=review.user.username) for review in results]