from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from src.books.domain.models import Rating, RatingScore, Review
from src.books.application.models import ReviewModel, RatingModel
# TODO: the repo shouldn't know about the api schemas 
from src.books.api.schemas.review_response import ReviewResponse

class AbstractReviewRepo(ABC):
    @abstractmethod
    def create_review(self, review: Review) -> None:
        """
        Create a new review in the repository.
        :param review: The review object to create.
        :return: None
        """
        pass

    @abstractmethod
    def get_reviews_by_book_id(self, book_id: UUID, sort_by: str = "date_created", sort_order: str = "desc", limit: int = 10) -> list[ReviewResponse]:
        """
        Get all reviews for a book.
        :param book_id: The ID of the book to get reviews for.
        :param limit: The number of reviews to return.
        :param sort_by: The field to sort the reviews by.
        :param sort_order: The order to sort the reviews by.
        :return: A list of review response objects.
        """ 
        pass

    @abstractmethod
    def get_reviews_by_user_id(self, user_id: UUID) -> list[ReviewResponse]:
        """
        Get all reviews for a user.
        :param user_id: The ID of the user to get reviews for.
        :return: A list of review response objects.
        """
        pass

    @abstractmethod
    def get_review_by_id(self, review_id: UUID) -> Review:
        """
        Get a review by its ID.
        :param review_id: The ID of the review to get.
        :return: A review response object.
        """
        pass

    @abstractmethod
    def get_review_by_rating_id(self, rating_id: UUID) -> Review:
        """
        Get a review by its associated rating's ID
        """
        pass

    @abstractmethod
    def get_review_by_user_and_book(self, user_id: UUID, book_id: UUID) -> ReviewResponse:
        """
        Get a review by user and book.
        :param user_id: The ID of the user.
        :param book_id: The ID of the book.
        :return: A review response object.
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
            .filter(ReviewModel.book_id == book_id, ReviewModel.date_deleted.is_(None))
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
        result = self.session.query(ReviewModel).filter(ReviewModel.user_id == user_id, ReviewModel.date_deleted.is_(None)).all()
        if not result:
            return []
        
        review_responses = []
        for review_model in result:
            review_response = self._create_review_response(review_model)
            if review_response:
                review_responses.append(review_response)
        
        return review_responses

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
    
    
    def get_review_by_user_and_book(self, user_id: UUID, book_id: UUID) -> ReviewResponse:
        result = self.session.query(ReviewModel).filter(
            ReviewModel.user_id == user_id, 
            ReviewModel.book_id == book_id
        ).first()
        if not result:
            return None
        return self._create_review_response(result)
    
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

    
