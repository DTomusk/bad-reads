from datetime import datetime, timezone
from pydantic import BaseModel, field_validator

class MeetingRequest(BaseModel):
    meeting_date: datetime

    @field_validator("meeting_date")
    @classmethod
    def validate_meeting_date(cls, v):
        
        currentDate = datetime.now(timezone.utc)
        if v > currentDate:
            raise ValueError("Meeting Date must be in the future")
        return v