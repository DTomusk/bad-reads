from pydantic import BaseModel, field_validator


class RateRequest(BaseModel):
    score: float
    review: str = None

    @field_validator("score")
    @classmethod
    def validate_score(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Score must be between 0 and 5")
        return v
    
    # TODO: review length of review
    @field_validator("review")
    @classmethod
    def validate_review(cls, v):
        if v is not None and len(v) > 1000:
            raise ValueError("Review must be less than 1000 characters")
        return v

