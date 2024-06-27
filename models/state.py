#!/usr/bin/python3
"""
Contains the class definition for State
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This class defines a state by various attributes"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete")

    @property
    def cities(self):
        from models import storage
        from models.city import City
        return [city for city in storage.all(City).values() if city.state_id == self.id]
