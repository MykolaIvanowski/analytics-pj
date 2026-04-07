from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class Metric(SQLModel, table=True):
    id: Optional[int]  = Field(default=None, primary_key =True)
    metric_name: str
    value: float
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
