#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = ""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    places = relationship("Place", cascade="delete", backref="cities")
