# Input van de keuze opslaan
VALID_CHOICES = {"1", "2", "3"}


def get_user_choice():
    choice = None
    while choice not in VALID_CHOICES:
        # Input van de keuze opslaan
        choice = input("Voer het nummer van uw keuze in: ")
        if choice not in VALID_CHOICES:
            print("Ongeldige keuze. Probeer het opnieuw")
    return int(choice)