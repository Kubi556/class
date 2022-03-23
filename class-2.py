import math
import pygame


class Postać:
    def __init__(self, nazwa):
        self.nazwa = "Torch Launcher"
        self.zycie = HP = 10
        self.umiejetnosci = []
        self.statystyki = {"sila": 5, "zwinność": 5, "kondycja": 7, "inteligencja": 6}
        print("Postać stworzona!")

    def przedstaw(self):
        print("Ta postać nazwya się ", self.nazwa, self.zycie, self.umiejetnosci, self.statystyki)

    def minusHP(self, hp):
        if (isinstance(hp, int) and hp < self.zycie): 
            self.zycie -= hp
            print("Straciłeś", hp, "zycia!")
            print("Zostało ci teraz")
            print(self.zycie)
            print("zycia")

        else: 
            print("Zginoles!")
        return self.zycie    

    def wzrostSila(self):
        self.statystyki["sila"] +=1
        print("Siła ci wzrasta")
        print("Nowa sila to")  
        print(self.statystyki["sila"])

    def stats(self):
        print("Lista statystyk: ", self.statystyki)    
    def dodajUmiejetnosc(self):
        self.umiejetnosci.append("nazwa")
        
        

rycerz = Postać("Torch Launcher") #konstruktor (__init___) jest uruchamiany przy 
                  #tworzeniu Postaci rycerz
                  #to sie chop przedstawia

        

rycerz.przedstaw() 
rycerz.minusHP(1)     
rycerz.dodajUmiejetnosc ("Skradanie sie")
rycerz.wzrostSila()






'''
print("##################   Funkcje z return   #####################")

prognoza = ""

prognoza = ""
def pogoda():
    #kod
    return "Bedzie padać snieg"
def pogoda2():
    prognoza = "Sniezyce, przelotne deszcze"
    return 0
def pogoda3(prognoza):
    return prognoza + "!"    

#pogoda2()
print(pogoda2())
print('############')
pogoda3("Deszcz") #odpdala funkcje, almie nie widac nic w konsoli
print(pogoda3("Deszcz"))
if (pogoda2() == 0):
    print("Hurra")'''