from fastapi import APIRouter, status
from models.models import User


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_201_CREATED)
async def ceate_user(user: User):
    return user


@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(user: User):
    return user
