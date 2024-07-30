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
        return f"{basis_beschrijving} met een brandstoftank inhoud van {self.brandstoftank_inhoud} liter"


def print_beschrijving(voertuig):
    print(voertuig.beschrijving())


# Maak een object van de class Auto
# mijn_auto = Auto("Toyota", "Corolla", 2020)
elektrische_auto = ElektrischeAuto("Tesla", "Model S", 2024, 100)
brandstof_auto = BrandstofAuto("Ford", "Mustang", 2021, 60)

autos = [elektrische_auto, brandstof_auto]

# Gebruik de methoden van de class
for auto in autos:
    print_beschrijving(auto)
    print(auto.versnel(30))
    print(auto.rem(10))
    print(auto.rem(25))
    print("\n")
