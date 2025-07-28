from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.bookclubs.domain.models import Meeting


class AbstractMeetingRepo(ABC):
    @abstractmethod
    def get_meeting_by_id(self, meeting_id: UUID) -> Meeting:
        """
        Get a meeting by its ID.
        :param meeting_id: The ID of the meeting to retrieve.
        :return: The meeting object.
        """

    @abstractmethod
    def get_meetings_by_book_club_id(self, book_club_id: UUID, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Meeting]:
        """
        Get all meetings.
        :param book_club_id: The id of the book club the meeting belongs to 
        :param page: The page number to retrieve.
        :param page_size: The number of meetings per page.
        :param sort_by: The field to sort the meetings by.
        :param sort_order: The order to sort the meetings by.
        :return: A list of meeting objects.
        """

    @abstractmethod 
    def add_meeting(self, meeting: Meeting) -> Meeting:
        """
        Add a meeting to the repository.
        :param meeting: The meeting object to add.
        :return: The added meeting object.
        """
    