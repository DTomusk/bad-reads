from pydantic import BaseModel, field_validator


class RateRequest(BaseModel):
    score: float

    @field_validator("score")
    @classmethod
    def validate_score(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Score must be between 0 and 5")
        return v

