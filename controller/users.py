from fastapi import APIRouter, Depends, status, HTTPException
from models.models import User
from database.database import SessionLocal
from sqlalchemy.orm import session
from database.models import UserDB
import uuid


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("", status_code=status.HTTP_201_CREATED)
def ceate_user(user: User, db: session = Depends(get_db)):
    if user is not None:
        try:
            uuid_gen = str(uuid.uuid4())
            new_user = UserDB(uuid=uuid_gen, first_name=user.first_name, last_name=user.last_name, email=user.email)
            db.add(new_user)
            db.commit()
            user.uuid = uuid_gen
            return user
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(user: User, db: session = Depends(get_db)):
    return user
