from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.books.domain.models import Rating


class RatingRepo(ABC):
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