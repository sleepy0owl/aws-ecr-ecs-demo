from fastapi import APIRouter, status
from models.models import Unicorn


router = APIRouter(
    prefix="/unicorns",
    tags=["unicorns"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_unicorn(unicorn: Unicorn):
    return unicorn


@router.get("", status_code=status.HTTP_200_OK)
async def get_unicorns():
    return [{
        "uuid": "26981737-0d6c-11ed-a8b9-1266feb9a66d",
        "name": "UnicornFloat",
        "description": "Big Unicorn Float! Giant Glitter Unicorn Pool Floaty",
        "price": 100,
        "image": "UnicornFloat"
    }]
