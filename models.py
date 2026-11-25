
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    city: Mapped[int] = mapped_column(
        String(100),
        nullable = False
    )
