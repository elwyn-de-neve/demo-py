# Definieer de tarieven per kilometer voor elk type Uber
    # Tarief per kilometer voor Uber Black
    # Tarief per kilometer voor Uber Van
    # Tarief per kilometer voor Uber X

# Vraag de gebruiker om het type Uber te kiezen

# Lees de keuze van de gebruiker in

# Vraag de gebruiker om het aantal kilometers in te voeren

# Bereken de kosten op basis van de keuze van de gebruiker
    # Als de gebruiker voor Uber Black kiest
    # Als de gebruiker voor Uber Van kiest
    # Als de gebruiker voor Uber X kiest
    # Als de gebruiker een ongeldige keuze maakt

# Print het resultaat


###############################################################


# Definieer de tarieven per kilometer voor elk type Uber
UBER_BLACK_RATE = 2.00  # Tarief per kilometer voor Uber Black
UBER_VAN_RATE = 3.50    # Tarief per kilometer voor Uber Van
UBER_X_RATE = 1.50      # Tarief per kilometer voor Uber X

# Vraag de gebruiker om het type Uber te kiezen
print("Kies het type Uber:")
print("1. Uber Black")
print("2. Uber Van")
print("3. Uber X")
print("---------------")

# Lees de keuze van de gebruiker in
choice = int(input("Voer het nummer van uw keuze in: "))

# Vraag de gebruiker om het aantal kilometers in te voeren
kilometers = int(input("Voer het aantal kilometers van uw rit in: "))

# Bereken de kosten op basis van de keuze van de gebruiker
if choice == 1:
    # Als de gebruiker voor Uber Black kiest
    cost = kilometers * UBER_BLACK_RATE
    uber_type = "Uber Black"
elif choice == 2:
    # Als de gebruiker voor Uber Van kiest
    cost = kilometers * UBER_VAN_RATE
    uber_type = "Uber Van"
elif choice == 3:
    # Als de gebruiker voor Uber X kiest
    cost = kilometers * UBER_X_RATE
    uber_type = "Uber X"
else:
    # Als de gebruiker een ongeldige keuze maakt
    print("Ongeldige keuze. Probeer het opnieuw.")
    cost = 0
    uber_type = "geen geldige keuze"

# Print het resultaat
if cost > 0:
    print(f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers} kilometer(s) zijn €{cost:.2f}.")
else:
    print("Er is een fout opgetreden. Geen kosten berekend.")
