from typing import List
from fastapi import APIRouter, Depends, status
from models.models import Unicorn
from database.database import SessionLocal
from sqlalchemy.orm import session
from database.models import UnicornsDB


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/unicorns",
    tags=["unicorns"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_unicorn(unicorn: Unicorn):
    return unicorn


@router.get("", status_code=status.HTTP_200_OK, response_model=List[Unicorn])
async def get_unicorns(db: session = Depends(get_db)):
    response = db.query(UnicornsDB).all()
    return response
