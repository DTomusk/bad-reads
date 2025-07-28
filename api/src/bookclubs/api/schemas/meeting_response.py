from src.books.domain.models import Book
from pydantic import BaseModel, ConfigDict
from src.bookclubs.domain.models import BookClub, Meeting
from uuid import UUID
import datetime

class MeetingResponse(BaseModel):
    id: UUID
    book_club_id: UUID
    date_created: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_domain(cls, book: Book, meeting: Meeting, book_club: BookClub) -> "MeetingResponse":
        return cls(
            id=str(meeting.id),
            book_id=book.id,
            book_club_id=book_club.id,
            meeting=meeting.id
        )