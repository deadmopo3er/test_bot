from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date)
    time = Column(Time)
    location = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"<Event(title={self.title}, date={self.date}, time={self.time}, location={self.location}, description={self.description})>"
