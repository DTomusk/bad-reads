from sqlalchemy import UUID
from sqlalchemy.orm import Session

from src.bookclubs.application.repositories.book_club_repo import AbstractBookClubRepo
from src.bookclubs.domain.models import BookClub
from src.bookclubs.infrastructure.models import BookClubModel


class BookClubRepo(AbstractBookClubRepo):
    def __init__(self, session: Session):
        self.session = session
    

    def _create_book_club(self, book_club: BookClub) -> BookClubModel:
        """
        Create a BookClubModel    
        """
        book_club_model = BookClubModel(
            id=book_club.id,
            name=book_club.name,
        )
        return book_club_model
    
    def get_book_club_by_id(self, book_club_id: UUID) -> BookClub:
        """
        Get a book_club by its ID.
        :param book_id: The ID of the book_club to retrieve.
        :return: The book_club object.
        """
        result = self.session.query(BookClubModel).filter(BookClubModel.id == book_club_id).first()
        if result:
            return self._create_book_club(result)
    
    def get_book_clubs(self, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[BookClub]:
        """
        Get all book_clubs.
        :return: A list of book_club objects.
        """
        result = (self.session.query(BookClubModel)
            .order_by(getattr(BookClubModel, sort_by).asc() if sort_order == "asc" else getattr(BookClubModel, sort_by).desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all())
        return [self._create_book_club(book_club) for book_club in result]
       
    def add_book_club(self, book_club: BookClub) -> BookClub:
        """
        Add a book_club to the repository.
        :param book_club: The book_club object to add.
        :return: The added book_club object.
        """
        existing_book_club = self.get_book_club_by_id(book_club.id)
        if existing_book_club:
            return existing_book_club
        self.session.add(self._create_book_club(book_club))
        self.session.commit()