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
            self.snelheid =
        return f"De {self.merk} {self.model} vertraagt naar {self.snelheid} km/u."


class ElektrischeAuto(Auto):
    def __init__(self, merk, model, bouwjaar, batterij_capaciteit):
        super().__init__(merk, model, bouwjaar)
        self.batterij_capaciteit = batterij_capaciteit

    def beschrijving(self):
        basis_beschrijving = super().beschrijving()
        return f"{basis_beschrijving} met een batterijcapaciteit van {self.batterij_capaciteit} kWh"


class BrandstofAuto(Auto):
    def __init__(self, merk, model, bouwjaar, brandstoftank_inhoud):
        super().__init__(merk, model, bouwjaar)
        self.brandstoftank_inhoud = brandstoftank_inhoud

    def beschrijving(self):
        basis_beschrijving = super().beschrijving()
        return f"{basis_beschrijving} met een brandstoftankinhoud van {self.brandstoftank_inhoud} liter"


# Functie die polymorfisme demonstreert
def print_beschrijving(auto):
    print(auto.beschrijving())


# Maak objecten van de subklassen
elektrische_auto = ElektrischeAuto("Tesla", "Model S", 2022, 100)
brandstof_auto = BrandstofAuto("Ford", "Mustang", 2021, 60)

# Gebruik polymorfisme met objecten van verschillende klassen
autos = [elektrische_auto, brandstof_auto]

for auto in autos:
    print_beschrijving(auto)
    print(auto.versnel(50))
    print(auto.rem(20))
    print()
