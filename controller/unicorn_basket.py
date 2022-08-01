from fastapi import APIRouter, Depends, HTTPException, status
from models.models import UnicornBasket
from database.database import SessionLocal
from sqlalchemy.orm import session
from database.models import UnicornBasketDB, UnicornsDB


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


@router.get("/{user_uuid}", status_code=status.HTTP_200_OK, response_model=UnicornBasket)
async def get_basket_by_user(user_uuid: str, db: session = Depends(get_db)):
    if user_uuid is not None:
        response = db.query(UnicornBasketDB).filter(UnicornBasketDB.uuid == user_uuid).all()
        if response:
            unicorn_uuid = response[0].unicornUuid
            unicorns = db.query(UnicornsDB).filter(UnicornsDB.uuid == unicorn_uuid).all()

            response_value = UnicornBasket(uuid=user_uuid, unicorns=unicorns)
            return response_value
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_basket(unicorn_basket: UnicornBasket, db: session = Depends(get_db)):
    if unicorn_basket is not None:
        user_uuid = unicorn_basket.uuid
        response = db.query(UnicornBasketDB).filter(UnicornBasketDB.uuid == user_uuid).all()
        if response:
            db.query(UnicornBasketDB).filter(UnicornBasketDB.uuid == user_uuid).delete()
            db.commit()

            return
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
