from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class CarModel(Base):
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(30))
    model: Mapped[str] = mapped_column(String(30))
    year: Mapped[int] = mapped_column(Integer)
    engine: Mapped[str] = mapped_column(String(30))
    fuel_type: Mapped[str] = mapped_column(String(30))
    color: Mapped[str] = mapped_column(String(30))
    mileage_km: Mapped[int] = mapped_column(Integer)
    number_of_doors: Mapped[int] = mapped_column(Integer)
    transmission: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float)
