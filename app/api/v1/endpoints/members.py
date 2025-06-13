from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....database import get_db
from ....models import Member
from ....schemas.member import MemberCreate, MemberRead, MemberUpdate

router = APIRouter(prefix="/members", tags=["members"])


@router.get("/", response_model=list[MemberRead])
def read_members(
    name: str | None = None,
    email: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Member)
    if name:
        query = query.filter(Member.name.ilike(f"%{name}%"))
    if email:
        query = query.filter(Member.email.ilike(f"%{email}%"))
    return query.all()


@router.post("/", response_model=MemberRead, status_code=201)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    db_member = Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.get("/{member_id}", response_model=MemberRead)
def read_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@router.put("/{member_id}", response_model=MemberRead)
def update_member(member_id: int, member_update: MemberUpdate, db: Session = Depends(get_db)):
    member = db.query(Member).get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    update_data = member_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(member, key, value)
    db.commit()
    db.refresh(member)
    return member


@router.delete("/{member_id}", status_code=204)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    db.delete(member)
    db.commit()
    return None
