from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.bookclubs.domain.models import BookClub


class AbstractBookClubRepo(ABC):
    @abstractmethod
    def get_book_club_by_id(self, book_club_id: UUID) -> BookClub:
        """
        Get a book_club by its ID.
        :param book_id: The ID of the book_club to retrieve.
        :return: The book_club object.
        """

    @abstractmethod
    def get_book_clubs(self, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[BookClub]:
        """
        Get all book_clubs.
        :param page: The page number to retrieve.
        :param page_size: The number of book_clubs per page.
        :param sort_by: The field to sort the book_clubs by.
        :param sort_order: The order to sort the book_clubs by.
        :return: A list of book_club objects.
        """

    @abstractmethod 
    def add_book_club(self, book_club: BookClub) -> BookClub:
        """
        Add a book_club to the repository.
        :param book_club: The book_club object to add.
        :return: The added book_club object.
        """
