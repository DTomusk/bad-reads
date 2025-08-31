from uuid import UUID
from src.bookclubs.api.schemas.meeting_request import MeetingRequest
from src.bookclubs.api.dependencies import create_meeting_use_case, get_book_club_details_use_case, get_book_clubs_use_case, get_meetings_by_book_club_use_case
from src.books.api.schemas.rate_request import RateRequest
from fastapi import APIRouter, Depends



router = APIRouter()

@router.get("")
async def get_book_clubs(get_book_clubs=Depends(get_book_clubs_use_case), page: int = 1, page_size: int = 10, sort_by: str = "name", sort_order: str = "asc", author_id: UUID = None):
    """
    Get all book_clubs.
    """
    book_clubs = get_book_clubs.execute(page, page_size, sort_by, sort_order)
    return book_clubs

@router.get("/{book_club_id}")
async def get_book_club_details(book_club_id: UUID, get_book_club_details=Depends(get_book_club_details_use_case)):
    """
    Get details of a book_club by its ID.
    """
    book_details = get_book_club_details.execute(book_club_id=book_club_id)
    return book_details

@router.get("/{book_club_id}/meetings")
async def get_meetings(book_club_id: UUID, get_meeting_by_book_club=Depends(get_meetings_by_book_club_use_case)):
    """
    Get details of a meetings by its book club id.
    """
    meetings = get_meeting_by_book_club.execute(book_club_id=book_club_id)
    return meetings

@router.post("/{book_club_id}/meeting")
async def new_book_club_meeting(
        book_club_id: UUID, 
        meeting_request: MeetingRequest,
        new_meeting=Depends(create_meeting_use_case)
    ):
    """
    Add a meeting to an existing book club
    """
    new_meeting.execute(book_club_id=book_club_id, meeting_date=meeting_request.meeting_date)
    return {"message": "Book club meeting added successfully"}