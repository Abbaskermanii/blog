from fastapi import FastAPI
from routers.users import router as user_routers

app = FastAPI()

app.include_router(user_routers , prefix="/users")
