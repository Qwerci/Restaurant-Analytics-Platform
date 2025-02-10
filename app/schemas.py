from pydantic import BaseModel
from typing import List, Optional

class RestaurantCreate(BaseModel):
    name: str
    location: str
    cuisine: str
    dishes: List[str]
    rating: float
    price_range: str
    has_delivery: bool

class AnalyticsResponse(BaseModel):
    top_cuisines: dict
    avg_rating: float
    popular_dishes: dict
    price_distribution: dict
