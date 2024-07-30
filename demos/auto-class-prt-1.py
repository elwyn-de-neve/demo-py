class Auto:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.snelheid = 0

    def beschrijving(self):
        return f"{self.merk} {self.model} uit {self.bouwjaar}"

    def versnel(self, toename):
        self.snelheid += toename
        return f"De {self.merk} {self.model} versnelt naar {self.snelheid} km/u."

    def rem(self, afname):
        self.snelheid -= afname
        if self.snelheid < 0:
            self.snelheid = 0
        return f"De {self.merk} {self.model} vertraagt naar {self.snelheid} km/u."


# Maak een object van de class Auto
mijn_auto = Auto("Toyota", "Corolla", 2020)

# Gebruik de methoden van de class
print(mijn_auto.beschrijving())
print(mijn_auto.versnel(30))
print(mijn_auto.rem(10))
print(mijn_auto.rem(25))
