from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict


class FuelTypeEnum(str, Enum):
    gasolina = "gasolina"
    álcool = "álcool"
    flex = "flex"
    diesel = "diesel"
    elétrico = "elétrico"
    híbrido = "híbrido"


class TransmissionEnum(str, Enum):
    manual = "manual"
    automatico = "automatico"
    cvt = "cvt"
    automatizado = "automatizado"


class CarSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    engine: Optional[str] = None
    fuel_type: Optional[FuelTypeEnum] = None
    color: Optional[str] = None
    mileage_km: Optional[int] = None
    number_of_doors: Optional[int] = None
    transmission: Optional[TransmissionEnum] = None
    price: Optional[float] = None
