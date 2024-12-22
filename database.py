from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Flight

DATABASE_URL = "sqlite:///flights.db"  # database connection URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create table
Base.metadata.create_all(engine)

def save_flight(flight_data):
    session = SessionLocal()
    try:
        flight = Flight(
            status=flight_data["status"],
            flight_airline=flight_data["flight_airline"],
            from_location=flight_data["from_location"],
            from_airport=flight_data["from_airport"],
            from_depart_times=flight_data["from_depart_times"],
            from_scheduled=flight_data["from_scheduled"],
            from_actual=flight_data["from_actual"],
            from_terminal=flight_data["from_terminal"],
            from_gate=flight_data["from_gate"],
            to_location=flight_data["to_location"],
            to_airport=flight_data["to_airport"],
            to_arrival_times=flight_data["to_arrival_times"],
            to_scheduled=flight_data["to_scheduled"],
            to_actual=flight_data["to_actual"],
            to_terminal=flight_data["to_terminal"],
            to_gate=flight_data["to_gate"],
            to_baggage=flight_data["to_baggage"],
        )
        session.add(flight)
        session.commit()
        print("Flight data saved to database.")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def get_all_flights():
    session = SessionLocal()
    print("Retrieving all flights from the database:")
    flights = session.query(Flight).all()
    for flight in flights:
        print(flight)

if __name__ == "__main__":
    # Drop and recreate the database uncomment to clear and recreate db
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # print("Database schema recreated.")

    # Fetch and display all flights in db
    print("Retrieving all flights from the database:")
    get_all_flights()
