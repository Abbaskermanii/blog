from pydantic import BaseModel


class signin_input(BaseModel):
    username: str
    password: str
