from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import enum

DATABASE_URL = "sqlite:///./app_database.db"  # Must match the DB_NAME in db_setup.py

Base = declarative_base()

class SensorReading(Base):
    """
    SQLAlchemy model for sensor readings.
    Corresponds to the 'SensorReadings' table in the SQLite database.
    """
    __tablename__ = "SensorReadings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    temperature = Column(Float)
    humidity = Column(Float)
    sensor_name = Column(String)

    def __repr__(self):
        return f"<SensorReading(id={self.id}, timestamp={self.timestamp}, temp={self.temperature}, hum={self.humidity}, sensor='{self.sensor_name}')>"

class RelayStateEnum(enum.Enum):
    ON = "ON"
    OFF = "OFF"

class RelayState(Base):
    """
    SQLAlchemy model for relay states.
    Corresponds to the 'RelayStates' table in the SQLite database.
    """
    __tablename__ = "RelayStates"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    relay_name = Column(String)
    # The Enum type stores the string 'ON' or 'OFF' in the database.
    state = Column(Enum(RelayStateEnum), nullable=False)


    def __repr__(self):
        return f"<RelayState(id={self.id}, timestamp={self.timestamp}, relay='{self.relay_name}', state='{self.state.value}')>"

# Engine and Session setup (optional here, but good for testing or direct model usage)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """
    Creates all tables in the database that are defined by Base's subclasses.
    This is typically called once at application startup.
    """
    Base.metadata.create_all(bind=engine)
    print("SQLAlchemy models' tables created (if they didn't exist).")

if __name__ == "__main__":
    # This will create the tables based on SQLAlchemy models.
    # Note: db_setup.py also creates tables using raw SQL.
    # Running both is fine; CREATE TABLE IF NOT EXISTS is used in both.
    create_tables()

    # Example of how to use the models (optional, for testing)
    # from database.db_setup import initialize_database
    # initialize_database() # Ensure DB and tables from db_setup.py are there

    # db = SessionLocal()
    # new_reading = SensorReading(temperature=25.5, humidity=60.1, sensor_name="DHT22_Indoor")
    # new_relay_state = RelayState(relay_name="Main_Pump", state=RelayStateEnum.ON)
    # db.add(new_reading)
    # db.add(new_relay_state)
    # db.commit()
    # print("Sample data added.")

    # readings = db.query(SensorReading).all()
    # states = db.query(RelayState).all()
    # print("All sensor readings:", readings)
    # print("All relay states:", states)
    # db.close()
