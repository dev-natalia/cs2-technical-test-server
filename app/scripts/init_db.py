from sqlalchemy import create_engine
from app.models import Base

engine = create_engine("sqlite:///car_database.db")

Base.metadata.create_all(engine)

print("Banco criado com sucesso!")
