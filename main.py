from fastapi import FastAPI
from src.users.routers import auth_routers, register_routers, reset_password_routers, user_routers
from core.db import database

app = FastAPI()

app.include_router(
    auth_routers[0],
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    register_routers,
    prefix='/users',
    tags=['users']
)

app.include_router(
    reset_password_routers,
    prefix='/auth',
    tags=['auth']
)

app.include_router(
    user_routers,
    prefix='/users',
    tags=['users']
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()