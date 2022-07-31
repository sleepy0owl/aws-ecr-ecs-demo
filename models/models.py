from typing import List, Union
from pydantic import BaseModel


class User(BaseModel):
    uuid: Union[str, None] = None
    email: str
    firstname: str
    lastname: str

    class Config:
        orm_mode = True


class Unicorn(BaseModel):
    uuid: Union[str, None]
    description: Union[str, None] = None
    name: str
    price: int
    image: Union[str, None] = None

    class Config:
        orm_mode = True


class UnicornBasket(BaseModel):
    uuid: Union[str, None]
    unicorns: List[Unicorn]

    class Config:
        orm_mode = True
