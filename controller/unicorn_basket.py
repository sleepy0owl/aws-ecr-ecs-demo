from fastapi import APIRouter, status
from models.models import UnicornBasket

router = APIRouter(
    prefix="/unicorns/basket",
    tags=['unicorn_basket']
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_unicron_basket(unicorn_basket: UnicornBasket):
    return unicorn_basket


@router.get("/{user_uuid}", status_code=status.HTTP_200_OK)
async def get_basket_by_user(user_uuid: str):
    return {"uuid": user_uuid}


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_basket():
    return "deleted"
