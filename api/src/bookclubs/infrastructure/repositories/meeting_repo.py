from sqlalchemy import UUID
from src.bookclubs.application.repositories.meeting_repo import AbstractMeetingRepo
from src.bookclubs.domain.models import Meeting
from src.bookclubs.infrastructure.models import MeetingModel
from sqlalchemy.orm import Session

class MeetingRepo(AbstractMeetingRepo):
    def __init__(self, session: Session):
        self.session = session
    
    def _create_meeting(self, meeting: MeetingModel) -> Meeting:
        return Meeting(
            id=meeting.id, 
            book_id = meeting.book_id,
            book_club_id=meeting.book_club_id, 
            date=meeting.date
            ) 
      
    def get_meeting_by_id(self, meeting_id: UUID) -> Meeting:
        """
        Get a meeting by its ID.
        :param book_id: The ID of the book_club to retrieve.
        :return: The book_club object.
        """
        result = self.session.query(MeetingModel).filter(MeetingModel.id == meeting_id).first()
        if result:
            return self._create_meeting(result)
    
    def get_meetings_by_book_club_id(self, book_club_id: UUID, page: int = 1, page_size: int = 10, sort_by: str = "name", sort_order: str = "asc") -> list[Meeting]:
        """
        Get all meetings for a book_club.
        :param book_club_id: The ID of the book_club to get meetings for.
        :return: A list of meeting objects.
        """
        result = self.session.query(MeetingModel).filter(MeetingModel.book_club_id == book_club_id).all()
        return [self._create_meeting(result)
            for result in result]

    def create_meeting(self, meeting: Meeting):
        """
        Create a new meeting in the repository.
        :param meeting: The meeting object to create.
        :return: None
        """
        # meeting_model = self.create_meeting(meeting)
        meeting_model = MeetingModel(
            id=meeting.id,
            book_id=meeting.book_id,
            book_club_id=meeting.book_club_id,
            date=meeting.date,
        )
        self.session.add(meeting_model)
        self.session.commit()