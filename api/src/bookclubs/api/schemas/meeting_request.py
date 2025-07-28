import datetime
from pydantic import BaseModel, field_validator

class MeetingRequest(BaseModel):
    date: datetime

    @field_validator("meeting_date")
    @classmethod
    def validate_meeting_date(cls, v):
        
        currentDate = datetime.datetime.now()
        if v > currentDate:
            raise ValueError("Meeting Date must be in the future")
        return v