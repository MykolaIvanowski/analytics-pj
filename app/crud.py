from sqlmodel import Session, select
from models import Metric


def save_metrics(session: Session, metric_type: str, value: float):
    metric =  Metric(metric_type=metric_type, value=value)
    session.add(metric)
    session.commit()
    session.refresh(metric)
    return metric

def get_latest_metric(session: Session, metric_type: str):
    query = (select(Metric).where(Metric.metric_type == metric_type)
             .order_by(Metric.created_at.desc()))
    return session.exec(query).first()

