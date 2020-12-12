from fastapi_users.db.sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String
from sqlalchemy_utils import ChoiceType
from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    pass