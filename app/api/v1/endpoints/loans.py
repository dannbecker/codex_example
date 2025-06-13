from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....database import get_db
from ....models import Loan
from ....schemas.loan import LoanCreate, LoanRead, LoanUpdate

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get("/", response_model=list[LoanRead])
def read_loans(db: Session = Depends(get_db)):
    return db.query(Loan).all()


@router.post("/", response_model=LoanRead, status_code=201)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    db_loan = Loan(member_id=loan.member_id, book_id=loan.book_id)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


@router.get("/{loan_id}", response_model=LoanRead)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).get(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@router.put("/{loan_id}", response_model=LoanRead)
def update_loan(loan_id: int, loan_update: LoanUpdate, db: Session = Depends(get_db)):
    loan = db.query(Loan).get(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    update_data = loan_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(loan, key, value)
    db.commit()
    db.refresh(loan)
    return loan


@router.delete("/{loan_id}", status_code=204)
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).get(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    db.delete(loan)
    db.commit()
    return None
