from uuid import UUID
from src.bookclubs.api.schemas.book_club_detail_response import BookClubDetailResponse
from src.bookclubs.application.repositories.book_club_repo import AbstractBookClubRepo
from src.bookclubs.application.repositories.meeting_repo import AbstractMeetingRepo

class GetBookClubDetails:
    def __init__(self, book_club_repository: AbstractBookClubRepo, meeting_repository: AbstractMeetingRepo):
        self.book_club_repository = book_club_repository
        self.rating_repository = meeting_repository

    def execute(self, book_club_id: UUID) -> BookClubDetailResponse:
        """ Get book_club details by its ID """
        # Get the book_club details
        book_club = self.book_club_repository.get_book_club_by_id(book_club_id)
        if not book_club:
            raise ValueError("BookClub Club not found")
        
        # Get the reviews for the book_club
        meetings = self.meetings.get_meeting(book_club_id)

        return BookClubDetailResponse.from_domain(book_club, meetings)