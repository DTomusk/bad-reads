
from uuid import UUID, uuid4

from src.bookclubs.infrastructure.models import MeetingModel
from src.bookclubs.application.repositories.book_club_repo import AbstractBookClubRepo
from src.bookclubs.application.repositories.meeting_repo import AbstractMeetingRepo
from src.bookclubs.domain.models import BookClub, Meeting
import datetime

class AddMeeting:
    def __init__(self, book_club_repo: AbstractBookClubRepo, meeting_repo: AbstractMeetingRepo):
        self.book_club_repository = book_club_repo
        self.meeting_repository = meeting_repo


    def execute(self, book_club_id: UUID, meeting_date: datetime) -> BookClub:
        """ User Makes a meeting """
        # Check if the BookClub Club exists
        book_club = self.book_club_repository.get_book_club_by_id(book_club_id)
        if not book_club:
            raise ValueError("BookClub Club not found")
        
        new_meeting = Meeting(id=uuid4(), book_id="7ad41559-598d-4a76-9e5d-48c7245bffa9", book_club_id=book_club_id, date=meeting_date)
        self.meeting_repository.create_meeting(new_meeting)
        # book_club.add_meeting(new_meeting)
        # self.book_club_repository.update_book_club(book_club)
        return book_club