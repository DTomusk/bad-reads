from src.bookclubs.domain.models import BookClub
from src.bookclubs.api.schemas.meeting_response import MeetingResponse
from pydantic import BaseModel

class BookClubDetailResponse(BaseModel):
    id: str
    name: str
    meetings: list[MeetingResponse]

    @classmethod
    def from_domain(cls, book_club: BookClub) -> "BookClubDetailResponse":
        return cls(
            id=str(book_club.id),
            name=book_club.name,
        )