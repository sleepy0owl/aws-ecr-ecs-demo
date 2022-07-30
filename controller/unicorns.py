from fastapi import APIRouter

router = APIRouter(
    prefix="/unicorns",
    tags=["unicorns"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("")
async def get_unicorns():
    return fake_items_db


@router.post("/basket")
async def create_unicorn_basket():
    return fake_items_db
