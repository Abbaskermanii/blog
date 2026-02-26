from engin import Base, engine
from models import user

__all__ = [
    "Base",
    "user",
]

Base.metadata.create_all(bind=engine)
