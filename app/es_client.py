from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv
load_dotenv()

es_url = os.getenv("ES")
# es = Elasticsearch("http://elasticsearch:9200")

def sync_restaurant_to_es(restaurant: dict):
    es_url.index(index="restaurants", id=restaurant["id"], document=restaurant)