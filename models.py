
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MarketLog(Base):
    __tablename__ = 'market_logs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recordDate = Column(DateTime)
    price = Column(Float)
    volRemaining = Column(Integer)
    typeID = Column(Integer)
    range = Column(String)
    orderID = Column(Integer)
    volEntered = Column(Integer)
    minVolume = Column(Integer)
    bid = Column(Boolean)
    issueDate = Column(DateTime)
    duration = Column(Integer)
    stationID = Column(Integer)
    regionID = Column(Integer)
    solarSystemID = Column(Integer)
    jumps = Column(Integer)
