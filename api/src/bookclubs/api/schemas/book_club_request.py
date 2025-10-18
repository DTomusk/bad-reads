from pydantic import BaseModel


class BookClubRequest(BaseModel):
    name: str
    # member_num: int

