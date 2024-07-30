class Hond:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def blaf(self):
        print(f"{self.naam} zegt: Woef! Woef!")

    def verjaar(self):
        self.leeftijd += 1
        print(f"Gefeliciteerd! {self.naam} is nu {self.leeftijd} jaar oud.")


mijn_hond = Hond("Rex", 3)  # Maak een object van de class Hond

mijn_hond.blaf()
mijn_hond.verjaar()
