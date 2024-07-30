# Definieer de tarieven per kilometer voor elk type Uber
rates = [2.00, 3.50, 1.50]  # Tarieven voor Uber Black, Uber Van en Uber X
uber_types = ["Uber Black", "Uber Van", "Uber X"]  # Namen van de verschillende Uber-typen

# Vraag de gebruiker om het type Uber te selecteren
print("Kies het type Uber:")  # Print instructie voor de gebruiker om een type Uber te kiezen
for i in range(len(uber_types)):  # Itereer over de lijst van Uber-typen
    print(f"{i + 1}. {uber_types[i]}")  # Print elk type Uber met een bijbehorend nummer
print("------------")  # Print een scheidingslijn

# Input van de keuze opslaan
choice = int(input("Voer het nummer van uw keuze in: "))  # Lees de keuze van de gebruiker in als een integer

# Controleer de geldigheid van de keuze
while choice < 1 or choice > len(uber_types):  # Blijf vragen totdat een geldige keuze is gemaakt
    print("Ongeldige keuze. Probeer het opnieuw.")  # Informeer de gebruiker over een ongeldige keuze
    choice = int(input("Voer het nummer van uw keuze in: "))  # Vraag opnieuw om de keuze van de gebruiker

# Vraag de gebruiker om het aantal kilometers in te voeren
kilometers = int(input("Voer het aantal kilometers van uw rit in: "))  # Lees het aantal kilometers in als een integer

# Controleer de geldigheid van de invoer voor kilometers
while kilometers < 0:  # Blijf vragen totdat een positief aantal kilometers is ingevoerd
    print("Ongeldige invoer. Het aantal kilometers moet positief zijn.")  # Informeer de gebruiker over ongeldige invoer
    kilometers = int(input("Voer het aantal kilometers van uw rit in: "))  # Vraag opnieuw om het aantal kilometers

# Bereken de kosten op basis van de keuze van de gebruiker
cost = kilometers * rates[choice - 1]  # Bereken de kosten door het aantal kilometers te vermenigvuldigen met het tarief
uber_type = uber_types[choice - 1]  # Haal de naam van het gekozen Uber-type op basis van de keuze

# Print het resultaat
print(f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers} kilometer(s) zijn €{cost:.2f}.")  # Print het resultaat, inclusief gekozen Uber-type en kosten
