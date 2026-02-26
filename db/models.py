from sqlalchemy.orm import mapped_column, Mapped
from engin import Base


class user(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str | None] = mapped_column(
        unique=True, default=None, nullable=True
    )
    password: mapped_column[str] = mapped_column()
