import databases
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db import database

from .backends import jwt_authentication, auth_backends, SECRET
from .models import User
from . import schemas


users = User.__table__
user_db = SQLAlchemyUserDatabase(User, database, users)


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    schemas.User,
    schemas.UserCreate,
    schemas.UserUpdate,
    schemas.UserDB,
)

auth_routers = fastapi_users.get_auth_router(jwt_authentication),
register_routers = fastapi_users.get_register_router()
reset_password_routers = fastapi_users.get_reset_password_router(SECRET)
user_routers = fastapi_users.get_users_router()