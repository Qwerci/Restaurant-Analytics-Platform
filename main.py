# fastapi/main.py
from fastapi import FastAPI
from app.routes import restaurants, analytics
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(restaurants.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")