#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class """
    __tablename__ = "states"
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})
    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            FLcity = models.storage.all(models.classes['City']).values()
            return [city for city in FLcity if city.state_id == self.id]
