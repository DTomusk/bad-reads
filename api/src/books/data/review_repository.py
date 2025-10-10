from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from ..domain.models import Review
from .models import ReviewModel

class AbstractReviewRepo(ABC):
    @abstractmethod
    def create_review(self, review: Review):
        """
        Create a new review in the repository.
        :param review: The review object to create.
        :return: None
        """
        pass

    @abstractmethod
    def get_review_by_rating_id(self, rating_id: UUID) -> Review:
        """
        Get a review by its associated rating's ID
        """
        pass

    @abstractmethod
    def update_review(self, review_id: UUID, text: str):
        """
        Update the text of an existing review
        """
        pass

    @abstractmethod
    def delete_review(self, review_id: UUID):
        """
        Soft delete a review (set date_deleted column to now)
        """
        pass

class ReviewRepo(AbstractReviewRepo):
    def __init__(self, session: Session):
        self.session = session

    def create_review(self, review: Review):
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
    
    def get_review_by_rating_id(self, rating_id: UUID) -> Review:
        result = self.session.query(ReviewModel).filter(ReviewModel.rating_id == rating_id).first()
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
    
    # Updating a review also undeletes it
    def update_review(self, review_id: UUID, text: str):
        review_model = self.session.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if review_model is None:
            raise ValueError("Review not found")
        
        review_model.text = text
        review_model.date_deleted = None
        self.session.commit()

    def delete_review(self, review_id):
        review_model = self.session.query(ReviewModel).filter(ReviewModel.id == review_id).first()
        if review_model is None:
            raise ValueError("Review not found")
        
        review_model.date_deleted = datetime.now(timezone.utc)
        self.session.commit()

    
