from pydantic import BaseModel, field_validator


class RateRequest(BaseModel):
    love_score: float
    shit_score: float

    @field_validator("love_score")
    @classmethod
    def validate_love_score(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Score must be between 0 and 5")
        return v

    @field_validator("shit_score")
    @classmethod
    def validate_shit_score(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Score must be between 0 and 5")
        return v

