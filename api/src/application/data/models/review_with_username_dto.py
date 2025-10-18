from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReviewWithUsernameDTO:
    love_score: float
    shit_score: float
    text: str
    date_created: datetime
    username: str