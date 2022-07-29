from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
    uuid: str
    email: str
    firstname: str
    lastname: str

class Unicorn(BaseModel):
    uuid: str
    description: Union[str, None] = None
    name: str
    price: int
    image: Union[str, None] = None

class UnicornBasket(BaseModel):
    uuid: str
    unicorns: List[Unicorn]
