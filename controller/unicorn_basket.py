from fastapi import APIRouter, Depends, HTTPException, status
from models.models import UnicornBasket
from database.database import SessionLocal
from sqlalchemy.orm import session
from database.models import UnicornBasketDB


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/unicorns/basket",
    tags=['unicorn_basket']
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("", status_code=status.HTTP_200_OK)
async def create_unicron_basket(unicorn_basket: UnicornBasket, db: session = Depends(get_db)):
    if unicorn_basket.uuid is not None and unicorn_basket.unicorns is not None:
        unicorn_uuid = unicorn_basket.unicorns[0].uuid
        user_uuid = unicorn_basket.uuid

        new_unicorn_basket = UnicornBasketDB(uuid=user_uuid, unicornUuid=unicorn_uuid)
        db.add(new_unicorn_basket)
        db.commit()

        return
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/{user_uuid}", status_code=status.HTTP_200_OK)
async def get_basket_by_user(user_uuid: str):
    return {"uuid": user_uuid}


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_basket():
    return "deleted"
