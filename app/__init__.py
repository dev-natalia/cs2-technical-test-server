from sqlalchemy import create_engine
from app.models import Base

engine = create_engine("sqlite:///car_database.db")
