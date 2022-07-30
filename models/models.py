from typing import List, Union
from pydantic import BaseModel


class User(BaseModel):
    uuid: Union[str, None]
    email: str
    firstname: str
    lastname: str


class Unicorn(BaseModel):
    uuid: Union[str, None]
    description: Union[str, None] = None
    name: str
    price: int
    image: Union[str, None] = None


class UnicornBasket(BaseModel):
    uuid: Union[str, None]
    unicorns: List[Unicorn]
