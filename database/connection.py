from sqlmodel import SQLModel, Session, create_engine,select
from models.events import Event

database_file = "planners.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)
def get_session():
    with Session(engine_url) as session:
        yield session
def get_events(Event):
    return select(Event)
    