from abc import ABC, abstractmethod

from api.ratings.domain.models import Rating


class RatingRepo(ABC):
    @abstractmethod
    def get_rating_by_user_and_book(self, user_id: str, book_id: str):
        """
        Get a rating by user and book.
        :param user_id: The ID of the user who rated the book.
        :param book_id: The ID of the book that was rated.
        :return: The rating object.
        """
        pass

    @abstractmethod
    def create_rating(rating: Rating):
        """
        Create a new rating in the repository.
        :param rating: The rating object to create.
        :return: None
        """
        pass

    @abstractmethod
    def update_rating(rating: Rating):
        """
        Update a rating in the repository.
        :param rating: The rating object to update.
        :return: None
        """
        pass