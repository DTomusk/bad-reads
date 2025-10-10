from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class RatingWithReviewDTO:
    book_id: UUID
    user_id: UUID
    love_score: float
    shit_score: float
    text: str
    date_created: datetime

@dataclass
class ReviewWithBookDetailsDTO:
    love_score: float
    shit_score: float
    text: str
    book_id: UUID
    picture_url: str
    title: str
    