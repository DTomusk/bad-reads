import datetime
from uuid import UUID

class BookClub:
    """ Represents a BookClub Club """
    def __init__(self, id: UUID, book_club_id: UUID, name: str):
        self.id = id
        self.name = name

    
class Meeting:
    """ Represents a Meeting associated with a BookClub """
    def __init__(self, id: UUID, book_id: UUID, book_club_id: UUID, date: datetime):
        self.id = id
        self.book_id = "test"
        self.book_club_id = book_club_id
        self.date = date
