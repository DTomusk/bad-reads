from src.bookclubs.application.repositories.meeting_repo import AbstractMeetingRepo
from src.bookclubs.domain.models import Meeting

# Note: this is a generic use case to get meetings
# We'll want to have different use cases e.g. for popular meetings, new meetings, bad meetings, etc.
class GetMeetingsByBookClub:
    def __init__(self, meeting_repository: AbstractMeetingRepo):
        self.meeting_repository = meeting_repository

    def execute(
            self, 
            book_club_id,
            page: int = 1, 
            page_size: int = 10, 
            sort_order: str = "asc",
        ) -> list[Meeting]:
        return self.meeting_repository.get_meetings_by_book_club_id(book_club_id, page=page, page_size=page_size, sort_order=sort_order)