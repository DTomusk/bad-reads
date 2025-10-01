from abc import ABC
from uuid import UUID
from sqlalchemy.orm import Session, joinedload

from ...books.data.models import ReviewModel
from ..application.models.review_with_username_dto import ReviewWithUsernameDTO

class AbstractReviewWithUsernameReader(ABC):
    def get_reviews_for_book(book_id: UUID) -> list[ReviewWithUsernameDTO]:
        """
        
        """
        pass

class ReviewWithUsernameReader(AbstractReviewWithUsernameReader):
    def __init__(self, session: Session):
        self.session = session

    def get_reviews_for_book(self, book_id):
        results = (
            self.session.query(ReviewModel)
                .filter(ReviewModel.book_id == book_id)
                .options(
                    joinedload(ReviewModel.rating), 
                    joinedload(ReviewModel.user)
                )
                .all()
        )

        return [ReviewWithUsernameDTO(
            love_score=review.rating.love_score,
            shit_score=review.rating.shit_score,
            text=review.text,
            date_created=review.date_created,
            username=review.user.username) for review in results]