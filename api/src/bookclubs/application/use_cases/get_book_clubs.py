from src.bookclubs.application.repositories.book_club_repo import AbstractBookClubRepo
from src.bookclubs.domain.models import BookClub

# Note: this is a generic use case to get book_clubs
# We'll want to have different use cases e.g. for popular book_clubs, new book_clubs, bad book_clubs, etc.
class GetBookClubs:
    def __init__(self, book_club_repository: AbstractBookClubRepo):
        self.book_club_repository = book_club_repository

    def execute(
            self, 
            page: int = 1, 
            page_size: int = 10, 
            sort_by: str = "name", 
            sort_order: str = "asc",
        ) -> list[BookClub]:
        return self.book_club_repository.get_book_clubs(page, page_size, sort_by, sort_order)