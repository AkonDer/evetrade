import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Boolean, DateTime, String, Date
from config import *

# SQLAlchemy Model
Base = declarative_base()


class MarketLog(Base):
    __tablename__ = 'market_logs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recordDate = Column(Date)
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


def read_file_to_db(file_path, db_url='sqlite:///evetrade_data.db'):
    # Create engine and session
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Read file using pandas
    df = pd.read_csv(file_path)


    # Convert DataFrame to list of MarketLog objects
    records = df.to_dict(orient='records')
    market_logs = [MarketLog(**record) for record in records]

    # Add records to database session and commit
    session.add_all(market_logs)
    session.commit()

    # Close the session
    session.close()


# Replace with your actual file path
file_path = PATH_TO_LOG + 'The Forge-Mexallon-2023.11.27 172226.txt'

# Call the function
read_file_to_db(file_path)
