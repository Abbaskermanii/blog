from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers.users import router as user_routers
from db.engine import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_routers, prefix="/users")