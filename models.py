from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, default="N/A")
    flight_airline = Column(String, default="N/A")
    from_location = Column(String, default="N/A")
    from_airport = Column(String, default="N/A")
    from_depart_times = Column(String, default="N/A")
    from_scheduled = Column(String, default="N/A")
    from_actual = Column(String, default="N/A")
    from_terminal = Column(String, default="N/A")
    from_gate = Column(String, default="N/A")
    to_location = Column(String, default="N/A")
    to_airport = Column(String, default="N/A")
    to_arrival_times = Column(String, default="N/A")
    to_scheduled = Column(String, default="N/A")
    to_actual = Column(String, default="N/A")
    to_terminal = Column(String, default="N/A")
    to_gate = Column(String, default="N/A")
    to_baggage = Column(String, default="N/A")

    def __repr__(self):
        return (
            f"ID={self.id}, "
            f"Status='{self.status}', "
            f"Airline='{self.flight_airline}', "
            f"From='{self.from_location}', "
            f"From Airport='{self.from_airport}', "
            f"Depart Date='{self.from_depart_times}', "
            f"Scheduled Depart Time='{self.from_scheduled}', "
            f"Actual Depart Time='{self.from_actual}', "
            f"Depart Terminal='{self.from_terminal}', "
            f"Depart Gate='{self.from_gate}', "
            f"To='{self.to_location}', "
            f"To Airport='{self.to_airport}', "
            f"Arrival Date='{self.to_arrival_times}', "
            f"Scheduled Arrival='{self.to_scheduled}', "
            f"Actual Arrival='{self.to_actual}', "
            f"Arrival Terminal='{self.to_terminal}', "
            f"Arrival Gate='{self.to_gate}', "
            f"Baggage='{self.to_baggage}', "
        )
