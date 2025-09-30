from dataclasses import dataclass


@dataclass
class RatingWithReviewDTO:
    love_score: float
    shit_score: float
    text: str