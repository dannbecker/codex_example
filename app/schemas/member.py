from pydantic import BaseModel
from typing import Optional


class MemberBase(BaseModel):
    name: str
    email: str


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class MemberRead(MemberBase):
    id: int

    class Config:
        orm_mode = True
