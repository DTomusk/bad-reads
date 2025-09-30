from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReviewWithUsernameDTO:
    love_score: float
    shit_score: float
    review: str
    date_created: datetime