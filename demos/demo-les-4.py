# Definieer de tarieven per kilometer voor elk type Uber
UBER_RATES = {  # Creëer een dictionary met de tarieven per kilometer voor elk type Uber
    "Uber Black": 2.00,  # Tarief per kilometer voor Uber Black
    "Uber Van": 3.50,    # Tarief per kilometer voor Uber Van
    "Uber X": 1.50       # Tarief per kilometer voor Uber X
}

# Definieer een set met geldige keuzes
VALID_CHOICES = {"1", "2", "3"}  # Creëer een set met geldige keuzes

# Vraag de gebruiker om het type Uber te kiezen
print("Kies het type Uber:")  # Print de prompt voor het kiezen van het type Uber
print("1. Uber Black")  # Print optie 1 voor Uber Black
print("2. Uber Van")  # Print optie 2 voor Uber Van
print("3. Uber X")  # Print optie 3 voor Uber X
print("---------------")  # Print scheidingslijn

# Lees de keuze van de gebruiker in
choice = None  # Initialiseer de variabele voor de keuze van de gebruiker
while choice not in VALID_CHOICES:  # Loop zolang de keuze niet geldig is
    choice = input("Voer het nummer van uw keuze in: ")  # Vraag de gebruiker om een keuze in te voeren
    if choice not in VALID_CHOICES:  # Controleer of de keuze ongeldig is
        print("Ongeldige keuze. Probeer het opnieuw.")  # Print een foutmelding bij ongeldige keuze

# Converteer de keuze naar een integer
choice = int(choice)  # Converteer de geldige keuze naar een integer

# Vraag de gebruiker om het aantal kilometers in te voeren
kilometers = None  # Initialiseer de variabele voor het aantal kilometers
while kilometers is None:  # Loop zolang het aantal kilometers niet geldig is
    try:
        kilometers = int(input("Voer het aantal kilometers van uw rit in: "))  # Vraag de gebruiker om het aantal kilometers in te voeren en probeer dit om te zetten naar een integer
    except ValueError:  # Vang een fout op als de invoer geen geldig getal is
        print("Ongeldige invoer, voer alstublieft een geheel getal in.")  # Print een foutmelding bij ongeldige invoer

# Gebruik een dictionary om het type Uber en tarief te bepalen
choice_dict = {  # Creëer een dictionary om de keuze te koppelen aan het type Uber
    1: "Uber Black",  # Koppeling van keuze 1 aan "Uber Black"
    2: "Uber Van",  # Koppeling van keuze 2 aan "Uber Van"
    3: "Uber X"  # Koppeling van keuze 3 aan "Uber X"
}

# Bereken de kosten op basis van de keuze van de gebruiker
uber_type = choice_dict.get(choice, "geen geldige keuze")  # Haal het type Uber op uit de dictionary gebaseerd op de keuze
cost = kilometers * UBER_RATES.get(uber_type, 0)  # Bereken de kosten door het aantal kilometers te vermenigvuldigen met het tarief uit de dictionary

# Print het resultaat
if cost > 0:  # Controleer of de kosten groter zijn dan 0
    print(f"U heeft gekozen voor {uber_type}. De kosten voor uw rit van {kilometers} kilometer(s) zijn €{cost:.2f}.")  # Print het resultaat als de kosten geldig zijn
else:  # Als de kosten 0 zijn (ongeldige keuze)
    print("Er is een fout opgetreden. Geen kosten berekend.")  # Print een foutmelding bij ongeldige keuze
