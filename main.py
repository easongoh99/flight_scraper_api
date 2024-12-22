import logging
from fastapi import FastAPI
from scraper import get_flights
from database import save_flight

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/flight-info")
async def get_flight_info(
        airline_code: str,
        flight_number: int,
        year: int,
        month: int,
        date: int
):
    logger.info(f"API called with parameters: airline_code={airline_code}, flight_number={flight_number}, year={year}, month={month}, date={date}")

    try:
        # Scrape flight data
        flight_data = get_flights(airline_code, flight_number, year, month, date)

        if not flight_data:
            # error message when flight data is not found
            return {"error": "Failed to retrieve flight data."}

        # Save flight data to the database
        save_flight(flight_data)
        # logger.info("Flight data saved to the database.")

        return {
            "message": "Flight data retrieved and saved successfully.",
            "data": flight_data
        }

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}
