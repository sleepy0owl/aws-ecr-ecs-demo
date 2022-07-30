from fastapi import APIRouter

router = APIRouter(
    prefix="/unicorns/basket",
    tags=['unicorn', "basket"]
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("")
async def create_unicron_basket():
    return fake_items_db


@router.get("/{user_uuid}")
async def get_basket_by_user():
    return fake_items_db


@router.delete("")
async def delete_basket():
    return "deleted"
