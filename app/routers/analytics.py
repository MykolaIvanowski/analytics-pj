from fastapi import APIRouter, Depends
from sqlmodel import Session
import httpx

from database import get_session
from crud import save_metric, get_latest_metric
from config import EVENT_COLLECTOR_URL


router = APIRouter(prefix="/analytics", tags=["Analytics"])

async def get_fetch_events(event_type: str | None = None):
    params = {}

    if event_type:
        params["event+type"] = event_type


    async with httpx.AsyncClient() as client:
        r  = await client.get(f"{EVENT_COLLECTOR_URL}/events", params=params)
        return r.json()

