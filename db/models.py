import uuid
from sqlalchemy.orm import Mapped, mapped_column
from db.engine import Base


class User(Base):
    __tablename__ = "users"

    password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(unique=True)
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
