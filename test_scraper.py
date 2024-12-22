from scraper import get_flights  # Import from scraper

def main():
    airline_code = "OS"
    flight_number = "302"
    year = "2024"
    month = "12"
    date = "20"

    flight_data = get_flights(airline_code, flight_number, year, month, date)

    # Print flight data
    if flight_data:
        print("Flight data fetched successfully:")
        print(f"Flight = {airline_code + " " + flight_number}")
        print(f"Airline = {flight_data['flight_airline']}")
        print(f"Flight Status = {flight_data['status']}\n")
        print("From:")
        print(f"Departure Location = {flight_data['from_location']}")
        print(f"Airport = {flight_data['from_airport']}")
        print(f"Flight Departure Date = {flight_data['from_depart_times']}")
        print(f"Scheduled Departure Time = {flight_data['from_scheduled']}")
        print(f"Actual Departure Time = {flight_data['from_actual']}")
        print(f"Terminal = {flight_data['from_terminal']}")
        print(f"Gate = {flight_data['from_gate']}\n")

        print("To:")
        print(f"Arrival Location = {flight_data['to_location']}")
        print(f"Airport = {flight_data['to_airport']}")
        print(f"Flight Arrival Date = {flight_data['to_arrival_times']}")
        print(f"Scheduled Arrival Time = {flight_data['to_scheduled']}")
        print(f"Actual Arrival Time = {flight_data['to_actual']}")
        print(f"Terminal = {flight_data['to_terminal']}")
        print(f"Gate = {flight_data['to_gate']}")
        print(f"Baggage = {flight_data['to_baggage']}")

    else:
        print("No flight data found")

main()