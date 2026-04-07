from pydentic import BaseModel

class MetricRead(BaseModel):
    metric_name: str
    value: float

    class Config:
        orm_mode = True