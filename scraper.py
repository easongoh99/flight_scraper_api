from bs4 import BeautifulSoup
import requests

def get_flights(airline_code, flight_number, year, month, date):
    # Construct URL
    url = f"https://www.flightstats.com/v2/flight-tracker/{airline_code}/{flight_number}?year={year}&month={month}&date={date}"
    print(f"Fetching URL: {url}")

    # Fetch page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Helper function to display N/A if element doesn't exist
    def safe_get_text(element):
        return element.get_text(strip=True) if element else "N/A"

    # Locate the flight information with div class name
    if soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 hYcdHE"):
        flight_status = soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 hYcdHE")
    else:
        flight_status = soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 iicbYn")

    if soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 ggStql"):
        flight_eta = soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 ggStql")
    else:
        flight_eta = soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 feVjck")

    flight_status_element = flight_status
    flight_eta_element = flight_eta
    flight_airline = soup.find("div", class_="text-helper__TextHelper-sc-8bko4a-0 eOUwOd")

    elements_location = soup.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 efwouT")
    elements_airport = soup.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 cHdMkI")
    elements_time = soup.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 kbHzdx")
    elements_terminal_gate = soup.find_all("div", class_="ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx")
    elements_depart_arrival = soup.find_all("div", class_="text-helper__TextHelper-sc-8bko4a-0 cPBDDe")

    # Strip data safely using safe_get_text
    flight_status_concat = safe_get_text(flight_status_element) if flight_status_element else "N/A"
    flight_eta_concat = safe_get_text(flight_eta_element) if flight_eta_element else "N/A"

    flight_status = flight_status_concat + " " + flight_eta_concat
    flight_airline = safe_get_text(flight_airline)

    flight_from_location = safe_get_text(elements_location[0]) if len(elements_location) > 0 else "N/A"
    flight_from_airport = safe_get_text(elements_airport[0]) if len(elements_airport) > 0 else "N/A"
    flight_from_depart_times = safe_get_text(elements_depart_arrival[0]) if len(elements_depart_arrival) > 0 else "N/A"
    flight_from_scheduled = safe_get_text(elements_time[0]) if len(elements_time) > 0 else "N/A"
    flight_from_actual = safe_get_text(elements_time[1]) if len(elements_time) > 1 else "N/A"
    flight_from_terminal = safe_get_text(elements_terminal_gate[0]) if len(elements_terminal_gate) > 0 else "N/A"
    flight_from_gate = safe_get_text(elements_terminal_gate[1]) if len(elements_terminal_gate) > 1 else "N/A"

    flight_to_location = safe_get_text(elements_location[1]) if len(elements_location) > 1 else "N/A"
    flight_to_airport = safe_get_text(elements_airport[1]) if len(elements_airport) > 1 else "N/A"
    flight_to_arrival_times = safe_get_text(elements_depart_arrival[1]) if len(elements_depart_arrival) > 1 else "N/A"
    flight_to_scheduled = safe_get_text(elements_time[2]) if len(elements_time) > 2 else "N/A"
    flight_to_actual = safe_get_text(elements_time[3]) if len(elements_time) > 3 else "N/A"
    flight_to_terminal = safe_get_text(elements_terminal_gate[2]) if len(elements_terminal_gate) > 2 else "N/A"
    flight_to_gate = safe_get_text(elements_terminal_gate[3]) if len(elements_terminal_gate) > 3 else "N/A"
    flight_to_baggage = safe_get_text(elements_terminal_gate[4]) if len(elements_terminal_gate) > 4 else "N/A"

    # Return the required values as key
    return {
        "status": flight_status,
        "flight_airline": flight_airline,
        "from_location": flight_from_location,
        "from_airport": flight_from_airport,
        "from_depart_times": flight_from_depart_times,
        "from_scheduled": flight_from_scheduled,
        "from_actual": flight_from_actual,
        "from_terminal": flight_from_terminal,
        "from_gate": flight_from_gate,
        "to_location": flight_to_location,
        "to_airport": flight_to_airport,
        "to_arrival_times": flight_to_arrival_times,
        "to_scheduled": flight_to_scheduled,
        "to_actual": flight_to_actual,
        "to_terminal": flight_to_terminal,
        "to_gate": flight_to_gate,
        "to_baggage": flight_to_baggage,
    }
