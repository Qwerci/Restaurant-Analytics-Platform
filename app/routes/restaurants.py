from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Restaurant
from app.schemas import RestaurantCreate
from ..database import get_db
from app.es_client import sync_restaurant_to_es

router = APIRouter()

@router.post("/restaurants/")
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    try:
        db_restaurant = Restaurant(**restaurant.model_dump())
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        sync_restaurant_to_es(restaurant.model_dump())
        return db_restaurant
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))