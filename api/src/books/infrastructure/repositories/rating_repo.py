from sqlalchemy import UUID
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.books.domain.models import Rating, RatingScore
from src.books.infrastructure.models import RatingModel
from sqlalchemy.orm import Session

class RatingRepo(AbstractRatingRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_rating_by_user_and_book(self, user_id: UUID, book_id: UUID) -> Rating:
        """
        Get a rating by user ID and book ID.
        :param user_id: The ID of the user.
        :param book_id: The ID of the book.
        :return: The rating object or None if not found.
        """
        result = (self.session.query(RatingModel)
            .filter(RatingModel.user_id == user_id, RatingModel.book_id == book_id)
            .first()
        )
        if result:
            return Rating(
                id=result.id,
                book_id=result.book_id,
                user_id=result.user_id,
                love_score=RatingScore(result.love_score),
                shit_score=RatingScore(result.shit_score)
            )
        return None
    
    def get_ratings_by_book_id(self, book_id: UUID) -> list[Rating]:
        """
        Get all ratings for a book.
        :param book_id: The ID of the book to get ratings for.
        :return: A list of rating objects.
        """
        result = self.session.query(RatingModel).filter(RatingModel.book_id == book_id).all()
        return [Rating(
            id=result.id, 
            book_id=result.book_id, 
            user_id=result.user_id, 
            love_score=RatingScore(result.love_score),
            shit_score=RatingScore(result.shit_score)
            ) 
            for result in result]

    def create_rating(self, rating: Rating):
        """
        Create a new rating in the repository.
        :param rating: The rating object to create.
        :return: None
        """
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
        """
        Update a rating in the repository.
        :param rating: The rating object to update.
        :return: None
        """
        rating_model = self.session.query(RatingModel).filter(RatingModel.id == rating.id).first()
        if rating_model:
            rating_model.love_score = rating.love_score.value
            rating_model.shit_score = rating.shit_score.value
            self.session.commit()
        else:
            raise ValueError("Rating not found")