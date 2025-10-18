from src.books.domain.models import Book
from pydantic import BaseModel, ConfigDict
from src.bookclubs.domain.models import BookClub, Meeting
from uuid import UUID
import datetime

class MeetingResponse(BaseModel):
    id: UUID
    book_club_id: UUID
    book_name: str = 'hardcoded'
    date: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_domain(cls, meeting: Meeting) -> "MeetingResponse":
        return cls(
            id=str(meeting.id),
            book_name='hardcoded',
            book_club_id=meeting.book_club_id,
            date=meeting.date
        )