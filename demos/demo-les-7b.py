import sys
import requests
import json

UBER_RATES = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}

VALID_CHOICES = {"1", "2", "3"}

API_URI = 'https://distanceto.p.rapidapi.com/distance/route/detailed'
HEADERS = {
    'Content-Type': 'application/json',
    'x-rapidapi-host': 'distanceto.p.rapidapi.com',
    'x-rapidapi-key': 'b3a4a2f9c5mshda14655e1c27d9bp111772jsn78c989f82758'
}

COUNTRY_CODE = "NLD"


def get_distance_in_kilometers(origin, destination):
    payload = {
        "route": [
            {
                "country": COUNTRY_CODE,
                "name": origin
            },
            {
                "country": COUNTRY_CODE,
                "name": destination
            }
        ]
    }
    try:
        response = requests.post(API_URI, json=payload, headers=HEADERS)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        kilometers = data['steps'][0]['distance']['car']['distance']
        return kilometers
    except requests.exceptions.RequestException as e:
        print(f"Fout bij het ophalen van de afstandsgegevens: {e}", file=sys.stderr)
        return None


def calculate_cost(choice, kilometers):
    if kilometers is None:
        return None, None

    choice_dict = {
        1: "Uber Black",
        2: "Uber Van",
        3: "Uber X"
    }
    uber_type = choice_dict.get(choice, "geen geldige keuze")
    cost = kilometers * UBER_RATES.get(uber_type, 0)
    return uber_type, cost


def display_result(uber_type, origin, destination, kilometers, cost):
    if cost is not None and cost > 0:
        print(
            f"U heeft gekozen voor {uber_type}. De afstand voor uw rit van {origin} naar {destination} met een afstand van {kilometers} kilometer(s) zijn €{cost:.2f}.",
            file=sys.stdout)
    else:
        print("Er is een fout opgetreden. Geen kosten berekend.", file=sys.stderr)


def read_input_from_stdin():
    try:
        data = json.load(sys.stdin)
        return data['choice'], data['origin'], data['destination']
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Fout bij het lezen van de invoer: {e}", file=sys.stderr)
        return None, None, None


def write_output_to_stdout(uber_type, origin, destination, kilometers, cost):
    try:
        output = {
            'uber_type': uber_type,
            'origin': origin,
            'destination': destination,
            'kilometers': kilometers,
            'cost': cost
        }
        json.dump(output, sys.stdout, indent=4)
        sys.stdout.write('\n')  # Ensure a newline at the end of the output
    except IOError as e:
        print(f"Fout bij het schrijven naar de uitvoer: {e}", file=sys.stderr)


def main():
    choice, origin, destination = read_input_from_stdin()
    if choice is None or origin is None or destination is None:
        print("Ongeldige invoer. Zorg ervoor dat de invoer correct is.", file=sys.stderr)
        return

    kilometers = get_distance_in_kilometers(origin, destination)
    uber_type, cost = calculate_cost(choice, kilometers)
    display_result(uber_type, origin, destination, kilometers, cost)
    write_output_to_stdout(uber_type, origin, destination, kilometers, cost)


main()
