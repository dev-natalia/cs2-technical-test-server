import random
from sqlalchemy.orm import Session

from app.models import CarModel
from app.scripts.init_db import engine

brand_model_map = {
    "Toyota": ["Corolla", "Hilux", "Etios"],
    "Honda": ["Civic", "Fit", "HR-V"],
    "Chevrolet": ["Onix", "Cruze", "S10"],
    "Ford": ["Ka", "Fusion", "Ranger"],
    "Volkswagen": ["Gol", "Polo", "T-Cross"],
}

with Session(engine) as session:
    for i in range(100):

        brand = random.choice(list(brand_model_map.keys()))
        model = random.choice(brand_model_map[brand])
        year = random.randint(2005, 2025)
        _engine = random.choice(
            [
                "1.0",
                "1.3",
                "1.6",
                "2.0",
                "1.0 Turbo",
                "1.4 Turbo",
                "1.8 Hybrid",
                "Elétrico",
            ]
        )
        fuel_type = random.choice(
            ["gasolina", "álcool", "flex", "diesel", "elétrico", "híbrido"]
        )
        color = random.choice(
            ["amarelo", "azul", "verde", "cinza", "prata", "branco", "preto"]
        )
        if year >= 2020:
            mileage_km = random.randint(0, 40000)
        elif year >= 2010:
            mileage_km = random.randint(40000, 120000)
        else:
            mileage_km = random.randint(120000, 250000)
        number_of_doors = random.randint(2, 5)
        transmission = random.choice(["manual", "automatico", "cvt", "automatizado"])
        if year >= 2020:
            price = random.randint(100000, 200000)
        elif year >= 2010:
            price = random.randint(50000, 120000)
        else:
            price = random.randint(30000, 90000)

        car = CarModel(
            brand=brand,
            model=model,
            year=year,
            engine=_engine,
            fuel_type=fuel_type,
            color=color,
            mileage_km=mileage_km,
            number_of_doors=number_of_doors,
            transmission=transmission,
            price=price,
        )
        session.add(car)
        print("Adicionado!")
    session.commit()
