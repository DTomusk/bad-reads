from pydantic import BaseModel

class RatingResponse(BaseModel):
    love_score: float
    shit_score: float