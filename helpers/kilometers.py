
# Vraag de gebruiker om het aantal kilometers in te voeren
def get_user_kilometers():
    kilometers = None
    while kilometers is None:
        # Vraag de gebruiker om het aantal kilometers in te voeren
        kilometers = int(input("Voer het aantal kilometers van uw rit in: "))
        if kilometers <= 0:
            print("Ongeldige invoer. Probeer het opnieuw")
            kilometers = None
    return kilometers