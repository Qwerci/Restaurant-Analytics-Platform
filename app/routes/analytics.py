# fastapi/app/routes/analytics.py
from fastapi import APIRouter, HTTPException
from ..es_client import es_url
from app.schemas import AnalyticsResponse
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/analytics/{location}", response_model=AnalyticsResponse)
def get_analytics(location: str):
    try:
        query = {
            "size": 0,
            "query": {"terms": {"location.keyword": location}},
            "aggs": {
                "top_cuisines": {"terms": {"field": "cuisine", "size": 5}},
                "avg_rating": {"avg": {"field": "rating"}},
                "popular_dishes": {"terms": {"field": "dishes", "size": 5}},
                "price_distribution": {"terms": {"field": "price_range"}}
            }
        }
        result = es_url.search(index="restaurants", body=query)
        logger.info("Elasticsearch query result: %s", result)
        return {
            "top_cuisines": result["aggregations"]["top_cuisines"]["buckets"],
            "avg_rating": result["aggregations"]["avg_rating"]["value"],
            "popular_dishes": result["aggregations"]["popular_dishes"]["buckets"],
            "price_distribution": result["aggregations"]["price_distribution"]["buckets"]
        }
    except Exception as e:
        logger.error("Error querying Elasticsearch: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
