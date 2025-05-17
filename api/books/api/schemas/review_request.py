from pydantic import BaseModel, field_validator

class ReviewRequest(BaseModel):
    text: str
    score: float

    @field_validator("score")
    @classmethod
    def validate_score(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Score must be between 0 and 5")
        return v

    @field_validator("text")
    @classmethod
    def validate_text(cls, v):
        if v is not None and len(v) > 1000:
            raise ValueError("Text must be less than 1000 characters")
        return v
    