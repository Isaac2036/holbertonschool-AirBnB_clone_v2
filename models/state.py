#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    hbnb_db = getenv("HBNB_MYSQL_DB")

    # For DB Storage
    if hbnb_db == "db":
        cities = relationship("City", backref="state", cascade="all,\
                delete-orphan")

    # For FileStorage
    else:
        @property
        def cities(self):
            from models import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
