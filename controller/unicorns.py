from fastapi import APIRouter
from models.models import Unicorn


router = APIRouter(
    prefix="/unicorns",
    tags=["unicorns"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("")
async def create_unicorn(unicorn: Unicorn):
    return unicorn


@router.get("")
async def get_unicorns():
    return fake_items_db
