from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("")
async def ceate_user():
    return fake_items_db


@router.post("/login")
async def user_login():
    return fake_items_db
