from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from src.infrastructure.db.database import Base

# Association table for the many-to-many relationship between book_club clubs and users
user_club_map = Table(
    "UserClubMap",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("users.id"), primary_key=True),
    Column("book_club_id", UUID, ForeignKey("book_clubs.id"), primary_key=True)
)

class BookClubModel(Base):
    __tablename__ = "book_clubs"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)

    meetings = relationship("MeetingModel", back_populates="book_clubs")


    def __repr__(self):
        return f"<BookClubModel(id={self.id}, name={self.name})>"
    
class MeetingModel(Base):
    __tablename__ = "meetings"

    id = Column(UUID, primary_key=True, index=True)
    book_club_id = Column(UUID, ForeignKey("book_clubs.id"), index=True)
    book_id = Column(String)
    date = Column(DateTime)

    book_clubs = relationship("BookClubModel", back_populates="meetings")
    # book = relationship("BookModel")


    def __repr__(self):
        return f"<MeetingModel(id={self.id}, book_id={self.book_id}, book_club_id={self.book_club_id}, date={self.date})>"