# from helpers.options import print_uber_options

UBER_RATES = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}

VALID_CHOICES = {"1", "2", "3"}


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


def get_user_kilometers():
    kilometers = None
    while kilometers is None:
        input_value = input("Voer het aantal kilometers van uw rit in: ")
        if input_value.isdigit():
            kilometers = int(input_value)
        else:
            print("Ongeldige invoer, voer alstublieft een geheel getal in.")
    return kilometers



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
            f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers} kilometer(s) zijn €{cost:.2f}.")
    else:
        print("Er is een fout opgetreden. Geen kosten berekend.")


def main():
    print_uber_options()
    choice = get_user_choice()
    kilometers = get_user_kilometers()
    uber_type, cost = calculate_cost(choice, kilometers)
    display_result(uber_type, kilometers, cost)


main()