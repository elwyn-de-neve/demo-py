# Print het resultaat
def display_result(uber_type, kilometers, cost):
    if cost > 0:
        print(f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers} kilometer(s) zijn €{cost}.")
    else:
        print("Er is een fout opgetreden. Er zijn geen kosten berekend.")