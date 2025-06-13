from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LoanBase(BaseModel):
    member_id: int
    book_id: int
    loan_date: Optional[datetime] = None
    return_date: Optional[datetime] = None


class LoanCreate(BaseModel):
    member_id: int
    book_id: int


class LoanUpdate(BaseModel):
    return_date: Optional[datetime] = None


class LoanRead(LoanBase):
    id: int

    class Config:
        orm_mode = True
