UBER_RATES = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}


def calculate_cost(choice, kilometers):
    choice_dict = {
        1: "Uber Black",
        2: "Uber Van",
        3: "Uber X"
    }
    uber_type = choice_dict.get(choice, "Geen geldige keuze")
    cost = kilometers * UBER_RATES.get(uber_type, 0)
    return uber_type, cost