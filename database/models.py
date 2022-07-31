from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "unicorn_users"
    id = Column(Integer(10), primary_key=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified_date = Column(DateTime(timezone=True), nullable=True)
    created_by_user_id = Column(Integer(10), nullable=True)
    last_modified_by_user_id = Column(Integer(10), nullable=True)
    active = Column(Boolean, default=True)
    uuid = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), nullable=False)
    first_name = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)


class Unicorns(Base):
    __tablename__ = "unicorns"
    id = Column(Integer(10), primary_key=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified_date = Column(DateTime(timezone=True), nullable=True)
    created_by_user_id = Column(Integer(10), nullable=True)
    last_modified_by_user_id = Column(Integer(10), nullable=True)
    active = Column(Boolean, default=True)
    uuid = Column(String(64), nullable=False)
    name = Column(String(64), nullable=True)
    description = Column(String(256), nullable=True)
    price = Column(Integer(10), nullable=True)
    image = Column(String(256), nullable=True)


class UnicornBasket(Base):
    __tablename__ = "unicorns_basket"
    id = Column(Integer(10), primary_key=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    last_modified_date = Column(DateTime(timezone=True), nullable=True)
    created_by_user_id = Column(Integer(10), nullable=True)
    last_modified_by_user_id = Column(Integer(10), nullable=True)
    active = Column(Boolean, default=True)
    uuid = Column(String(64), unique=True, nullable=False)
    unicornUuid = Column(String(64), unique=True, nullable=False)
