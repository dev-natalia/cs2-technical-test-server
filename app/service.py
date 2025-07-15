from typing import Dict
from sqlalchemy.orm import Session
import json

from app.schemas import CarSchema
from app.models import CarModel
from app import engine


class Service:
    def __init__(self, data: Dict):
        parsed = json.loads(data)
        self.data = CarSchema(**parsed)

    def execute(self):
        with Session(engine) as session:
            query = session.query(CarModel)
            for key, value in self.data.model_dump().items():
                if value is not None:
                    query = query.filter(getattr(CarModel, key) == value)
            results = query.all()

        return json.dumps([CarSchema.from_orm(car).model_dump() for car in results])
