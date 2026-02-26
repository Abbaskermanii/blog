from fastapi import APIRouter, Body, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.users import userOprations
from schemas._input import signin_input
from db.engine import get_db

router = APIRouter()


@router.get("/")
async def profile_users():
    return {"profile_users"}


@router.post("/signin")
async def signin(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: signin_input = Body(),
):
    user = userOprations(db_session).create(
        username=data.username, password=data.password
    )
    return data


@router.post("/login")
async def login():
    return {"login"}


@router.put("/")
async def update_profile():
    return {"update_profile"}
