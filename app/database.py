from sqlmodel import SQLModel, create_engine, Session
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.crete_all(engine)


def drop_db():
    with Session(engine) as session:
        yield session