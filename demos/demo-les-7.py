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


def print_uber_options():
    print("Kies het type Uber:")
    print("1. Uber Black")
    print("2. Uber Van")
    print("3. Uber X")
    print("---------------")


def get_user_choice():
    choice = None
    while choice not in VALID_CHOICES:
        choice = input("Voer het nummer van uw keuze in: ")
        if choice not in VALID_CHOICES:
            print("Ongeldige keuze. Probeer het opnieuw.")
    return int(choice)


def get_user_location(prompt):
    location = input(prompt)
    return location


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
        print(f"Fout bij het ophalen van de afstandsgegevens: {e}")
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
            f"U heeft gekozen voor {uber_type}. De afstand voor uw rit van {origin} naar {destination} met een afstand van {kilometers} kilometer(s) zijn €{cost:.2f}.")
    else:
        print("Er is een fout opgetreden. Geen kosten berekend.")


def read_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['choice'], data['origin'], data['destination']
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fout bij het lezen van het invoerbestand: {e}")
        return None, None, None


def write_output_to_file(file_path, uber_type, kilometers, cost):
    try:
        with open(file_path, 'w') as file:
            output = {
                'uber_type': uber_type,
                'kilometers': kilometers,
                'cost': cost
            }
            json.dump(output, file, indent=4)
    except IOError as e:
        print(f"Fout bij het schrijven naar het uitvoerbestand: {e}")


def main():
    input_file = '../input.json'
    output_file = '../output.json'

    choice, origin, destination = read_input_from_file(input_file)
    if choice is None or origin is None or destination is None:
        print("Ongeldige invoer. Zorg ervoor dat het invoerbestand correct is.")
        return

    kilometers = get_distance_in_kilometers(origin, destination)
    uber_type, cost = calculate_cost(choice, kilometers)
    display_result(uber_type, origin, destination,kilometers, cost)
    write_output_to_file(output_file, uber_type, kilometers, cost)


main()
