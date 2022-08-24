from fastapi import APIRouter, Depends
from app.core.schemas.user import UserBase
from app.core.models.user import User
from sqlalchemy.orm import Session
from app.core.models.database import get_db

router = APIRouter()

@router.post("/users", response_model=UserBase, tags=["users"])
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return __create_user(db, user)

@router.get("/users/{user_id}", response_model=UserBase, tags=["users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return __get_user(db, user_id)

def __get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def __create_user(db: Session, user: UserBase):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user