from fastapi import APIRouter, Depends
from sqlmodel import Session
import httpx

from database import get_session
from crud import save_metric, get_latest_metric
from config import EVENT_COLLECTOR_URL


router = APIRouter(prefix="/analytics", tags=["Analytics"])

async def fetch_events(event_type: str | None = None):
    params = {}

    if event_type:
        params["event+type"] = event_type


    async with httpx.AsyncClient() as client:
        r  = await client.get(f"{EVENT_COLLECTOR_URL}/events", params=params)
        return r.json()


@router.get("/items/popular")
async def popular_items(session: Session = Depends(get_session)):
    events = await fetch_events("item_created")

    count  = len(events)
    metric = save_metric(session, 'popular_items', count)
    return {"metric": metric.value}


@router.get("/users/activity")
async def users_activity(session: Session = Depends(get_session)):
    events =  await fetch_events("user_login")

    unique_users = len({e["user_id"] for e in events if e["user_id"]})
    metric = save_metric(session, "user_activity", unique_users)
    return {"metric": metric.value}

@router.get("/latest/metric_type")
async def latest_metric(metric_type: str, session: Session =  Depends(get_session)):
    metric  = get_latest_metric(session, metric_type)
    if not metric:
        return {"metric": None}
    return {"metric": metric.value}