import requests

UBER_RATES = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}

VALID_CHOICES = {"1", "2", "3"}

API_URL = 'https://distanceto.p.rapidapi.com/distance/route/detailed'
HEADERS = {
    'Content-Type': 'application/json',
    'x-rapidapi-host': 'distanceto.p.rapidapi.com',
    'x-rapidapi-key': 'b3a4a2f9c5mshda14655e1c27d9bp111772jsn78c989f82758'
}

NETHERLANDS_COUNTRY_CODE = "NLD"


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
                "country": NETHERLANDS_COUNTRY_CODE,
                "name": origin
            },
            {
                "country": NETHERLANDS_COUNTRY_CODE,
                "name": destination
            }
        ]
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        kilometers = data['steps'][0]['distance']['car']['distance']
        return kilometers  # Distance is already in kilometers
    else:
        print("Fout bij het ophalen van de afstandsgegevens.")


def calculate_cost(choice, kilometers):
    choice_dict = {
        1: "Uber Black",
        2: "Uber Van",
        3: "Uber X"
    }
    uber_type = choice_dict.get(choice, "geen geldige keuze")
    cost = kilometers * UBER_RATES.get(uber_type, 0)
    return uber_type, cost


def display_result(uber_type, kilometers, cost):
    if cost > 0:
        print(
            f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers:.2f} kilometer(s) zijn €{cost:.2f}.")
    else:
        print("Er is een fout opgetreden. Geen kosten berekend.")


def main():
    print_uber_options()
    choice = get_user_choice()
    origin = get_user_location("Voer uw huidige locatie (adres) in: ")
    destination = get_user_location("Voer uw bestemming (adres) in: ")

    kilometers = get_distance_in_kilometers(origin, destination)
    if kilometers is not None:
        uber_type, cost = calculate_cost(choice, kilometers)
        display_result(uber_type, kilometers, cost)
    else:
        print("Kan de afstand niet berekenen.")


main()
