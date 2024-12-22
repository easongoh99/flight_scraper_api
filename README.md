# Flight API
This project is a Python-based API for fetching and displaying flight information using FastAPI.

## Features
- Scrapes flight details from online sources.
- Stores data in a SQLite database using SQLAlchemy.
- Provides endpoints to query flight information.

## Requirements
- Python 3.9 or higher
- IntelliJ IDEA (Optional used for development)

## Installation
Download and Open Project

# In Terminal
cd to-project-path  
pip install -r dependencies.txt

## Run FastAPI server
uvicorn main:app --reload

## Example URL used in browser after successfuly Application startup
http://127.0.0.1:8000/flight-info?airline_code=OS&flight_number=302&year=2024&month=12&date=20  
http://127.0.0.1:8000/flight-info?airline_code=MU&flight_number=9783&year=2024&month=12&date=20  
http://127.0.0.1:8000/flight-info?airline_code=MS&flight_number=965&year=2024&month=12&date=22  
  
test_scraper.py run locally to test information scraping in Python Console  
database.py may run locally to display saved Flight data or delete and recreate table in database

