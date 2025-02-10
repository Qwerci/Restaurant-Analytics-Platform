import json
from faker import Faker
import random

fake = Faker()

cuisines = ["Italian", "Mexican", "Japanese", "Indian", "French"]
dishes = ["Pizza", "Sushi", "Tacos", "Pasta", "Burger"]
price_ranges = ["Budget", "Mid-Range", "High-End", "Luxury"]
cities = ["Paris", "Tokyo", "New York", "London", "Berlin"]

def generate_restaurants(num=1000):
    restaurants = []
    for _ in range(num):
        restaurant = {
            "id": str(fake.uuid4()),
            "name": fake.company(),
            "location": random.choice(cities),
            "cuisine": random.choice(cuisines),
            "dishes": random.sample(dishes, k=random.randint(1, 3)),
            "rating": round(random.uniform(3.0, 5.0), 1),
            "price_range": random.choice(price_ranges),
            "has_delivery": random.choice([True, False])
        }
        restaurants.append(restaurant)
    return restaurants

# Save to JSON for bulk indexing
with open("restaurants.json", "w") as f:
    for restaurant in generate_restaurants():
        f.write(json.dumps({"index": {"_index": "restaurants", "_id": restaurant["id"]}}) + "\n")
        f.write(json.dumps(restaurant) + "\n")