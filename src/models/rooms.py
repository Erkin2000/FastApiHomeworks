from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Column, Integer, Float, ForeignKey

from src.database import Base


class RoomsOrm(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    hotels_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    title: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[int]
    quantity: Mapped[int]
