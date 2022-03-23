import pygame
import math

#Tu są wszystkie klasy postaci
class Postać:
    def __init__ (self, name):
        self.name = "squirtle"
        self.zycie = 22
        self.umiejetnosci = ["wodny atak"]
        self.statystyki = {"sila": 9, "obrona": 2, "zwinnosc": 9}
        print("Pokemon zlapany!")

class Postać2:
    def __init__ (self, name):
        self.name = "charmander"
        self.zycie = 25
        self.umiejetnosci = ["ryk ognia"]
        self.statystyki = {"sila": 11, "obrona": 1, "zwinnosc": 3}
        print("Pokemon zlapany!")

class Postać3:
    def __init__ (self, name):
        self.name = "bulbazaur"
        self.zycie = 29
        self.umiejetnosci = ["ryk ognia"]
        self.statystyki = {"sila": 7, "obrona": 7, "zwinnosc": 1}
        print("Pokemon zlapany!")

########################################################################################################################        

#Tu sa różne funkce moga się przydać
    def przedstaw(self):
        print("Ten pokemon nazywa się ", self.name, "ma", self.zycie, "zycia", "jego umiejetnosci to:", self.umiejetnosci, "jego statystyki to:", self.statystyki)

    def minusHP(self, hp):
        if (isinstance(hp, int) and hp < self.zycie): 
            self.zycie -= hp
            print("Straciłeś", hp, "zycia!")
            print("Zostało ci teraz", self.zycie, "zycia")

    def atak(self):
        self.statystyki["sila"] 
        print("zadales", self.statystyki["sila"], "obrażeń")
        

##################################################################################################################        

     





















#Tu są komedy wykonawcze
poke1 = Postać("squirtle")
poke2 = Postać2("charmander")
poke3 = Postać3("bulbasaur")
poke1.przedstaw()



poke1.minusHP(1) 

poke1.atak()
################################################################################################################################

#???????????????????????????????????????????????????????????????//
print("wybierz pokemona")