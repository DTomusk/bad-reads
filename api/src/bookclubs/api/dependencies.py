from src.bookclubs.application.use_cases.add_meeting import AddMeeting
from src.bookclubs.application.use_cases.get_book_club_details import GetBookClubDetails
from src.bookclubs.application.use_cases.get_book_clubs import GetBookClubs
from src.bookclubs.application.use_cases.get_meetings_by_book_club import GetMeetingsByBookClub
from src.bookclubs.infrastructure.repositories.book_club_repo import BookClubRepo
from src.bookclubs.infrastructure.repositories.meeting_repo import MeetingRepo

from fastapi import Depends

from src.infrastructure.db.database import get_session

def get_book_clubs_repo(session=Depends(get_session)):
    """
    Dependency to provide the BookClub Clubs repository.
    """
    return BookClubRepo(session=session)

def get_meeting_repo(session=Depends(get_session)):
    """
    Dependency to provide the meeting repository.
    """
    return MeetingRepo(session=session)

def get_book_clubs_use_case(book_club_repo=Depends(get_book_clubs_repo)):
    """
    Dependency to provide the GetBookClubs use case.
    """
    return GetBookClubs(book_club_repository=book_club_repo)

def get_book_club_details_use_case(book_club_repo=Depends(get_book_clubs_repo), meeting_repo=Depends(get_meeting_repo)):
    """
    Dependency to provide the GetBookClubDetails use case.
    """
    return GetBookClubDetails(book_club_repository=book_club_repo, meeting_repository=meeting_repo)

def get_meetings_by_book_club_use_case(meeting_repo=Depends(get_meeting_repo)):
    """
    Dependency to provide the GetBookClubDetails use case.
    """
    return GetMeetingsByBookClub(meeting_repository=meeting_repo)

def create_meeting_use_case(book_club_repo=Depends(get_book_clubs_repo), meeting_repo=Depends(get_meeting_repo),):
    """
    Dependency to provide the add meeting use case.
    """
    return AddMeeting(book_club_repo=book_club_repo, meeting_repo=meeting_repo)

# def search_book_clubs_use_case(
#     book_repo=Depends(get_book_clubs_repo), 
#     external_book_clubs_service=Depends(get_external_book_clubs_service), 
#     author_repo=Depends(get_authors_repo), 
#     background_tasks: BackgroundTasks = None
# ):
#     """
#     Dependency to provide the SearchBooks use case.
#     """
#     return SearchBooks(
#         book_repository=book_repo, 
#         external_book_clubs_service=external_book_clubs_service, 
#         author_repository=author_repo, 
#         background_task_queue=FastAPIBackgroundTaskQueue(background_tasks=background_tasks)
#     )
