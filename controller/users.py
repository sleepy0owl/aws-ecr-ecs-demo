from fastapi import APIRouter
from models.models import User


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("")
async def ceate_user(user: User):
    return user


@router.post("/login")
async def user_login(user: User):
    return user
