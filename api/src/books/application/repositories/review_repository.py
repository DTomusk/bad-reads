from abc import ABC, abstractmethod
from uuid import UUID

from src.books.domain.models import Review


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
    def get_reviews_by_book_id(self, book_id: UUID) -> list[Review]:
        """
        Get all reviews for a book.
        :param book_id: The ID of the book to get reviews for.
        :return: A list of review objects.
        """ 
        pass

    @abstractmethod
    def get_reviews_by_user_id(self, user_id: UUID) -> list[Review]:
        """
        Get all reviews for a user.
        :param user_id: The ID of the user to get reviews for.
        :return: A list of review objects.
        """
        pass

    @abstractmethod
    def get_review_by_id(self, review_id: UUID) -> Review:
        """
        Get a review by its ID.
        :param review_id: The ID of the review to get.
        :return: A review object.
        """
        pass

    @abstractmethod
    def get_review_by_user_and_book(self, user_id: UUID, book_id: UUID) -> Review:
        """
        Get a review by user and book.
        """
        pass
