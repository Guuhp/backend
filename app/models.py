from pydantic import BaseModel
from typing import Optional


class ResponseBase(BaseModel):
    success: bool
    message: str


class SchoolOut(ResponseBase):
    data: dict


class Media(BaseModel):
    center: str
    title: str
    nasa_id: str
    date_created: str
    href: Optional[str] = None
