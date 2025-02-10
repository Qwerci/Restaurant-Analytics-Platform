from sqlalchemy import Column, String, Float, Boolean, ARRAY
from .database import Base
import uuid

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    location = Column(String)
    cuisine = Column(String)
    dishes = Column(ARRAY(String))
    rating = Column(Float)
    price_range = Column(String)
    has_delivery = Column(Boolean)