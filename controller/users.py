from fastapi import APIRouter, Depends, status
from models.models import User
from database.database import SessionLocal
from sqlalchemy.orm import session
from database.models import UserDB


def get_db():
    db = SessionLocal()
    print("accessed")
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_201_CREATED)
async def ceate_user(user: User, db: session = Depends(get_db)):
    user_1 = db.query(UserDB).all()
    print(user_1)
    return user


@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(user: User, db: session = Depends(get_db)):
    return user
