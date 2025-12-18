from random import random

sexe_bebe = 'M' if random() > 0.5 else 'F'

class Animal():

    def __init__(self, nom, age, sexe, espece) -> None:
        self.nom = nom
        self.age = age
        self.sexe = sexe        # "M" ou "F"
        self.espece = espece
        self.sante = 100
        self.energie = 100
        self.est_vivant = True

    def manger(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus manger")
            return False

        # Manger diminue l'énergie de 10
        if self.energie >= 10:
            self.energie -= 10
            print(f"{self.nom} mange (-10 énergie). Énergie restante : {self.energie}")
            self.verifier_vie()
            return True
        else:
            print(f"{self.nom} est trop fatigué pour manger.")
            return False
    def dormir(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus dormir")
            return

        # Dormir recharge 20 d'énergie, mais coûte 10 d'énergie (pour l'action)
        self.energie = min(100, self.energie - 10 + 20)  # net +10 max à 100
        print(f"{self.nom} dort (+20 énergie, -10 énergie action). Énergie actuelle : {self.energie}")
        self.verifier_vie()

    def soigner(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus être soigné")
            return
        self.sante = min(100, self.sante + 30)
        print(f"{self.nom} a été soigné (+30 santé). Santé actuelle : {self.sante}")

    def vieillir(self):
        if not self.est_vivant:
            print(f"{self.nom} est déjà mort :( ")
            return
        self.age += 1
        perte_sante = self.sante * 0.05  # 5% de perte de santé par année
        self.sante -= perte_sante
        print(f"{self.nom} vieillit d'un an (-5% santé). Âge: {self.age}, Santé : {self.sante:.1f}")
        self.verifier_vie()

    def verifier_vie(self):
        if self.sante <= 0:
            self.est_vivant = False
            self.sante = 0
            print(f"{self.nom} est mort...")

    def peut_se_reproduire(self):
        return self.age >= 2 and self.est_vivant == True

    def reproduire(self, autre_animal):
        if not self.peut_se_reproduire() or not autre_animal.peut_se_reproduire():
            return None

        if self.sexe == autre_animal.sexe:
            return None

        if self.espece != autre_animal.espece:
            return None

        nom_bebe = f"{self.nom[:3]}{autre_animal.nom[:3]}"
        sexe_bebe = 'M' if random() > 0.5 else 'F'

        return Animal(nom_bebe, 0, sexe_bebe, self.espece)

    def __str__(self) -> str:
        return f"nom : {self.nom}, age : {self.age}, sexe : {self.sexe}"
    
    def __eq__(self, value) -> bool:
        return self.nom == value.nom and self.age == value.age
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >= 0:
            self.age = age


class Chien(Animal):
    chien_img = """
  / \\__
 (    @\\___
 /         O
/   (_____/
 /_____/   U
"""

    def __init__(self, nom, age, sexe, race) -> None:
        Animal.__init__(self, nom, age, sexe, "chien")
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie : Woof ! Woof !")

    def reproduire(self, autre_animal):
        bebe = super().reproduire(autre_animal)
        if bebe:
            return Chien(bebe.nom, 0, bebe.sexe, self.race)
        return None

    def __str__(self) -> str:
        parent_str = Animal.__str__(self)
        return f"{parent_str}, race : {self.race}"


class Chat(Animal):
    chat_img = """
 /\\_/\\
( o.o )
 > ^ <
"""
    def __init__(self, nom, age, sexe, couleur) -> None:
        Animal.__init__(self, nom, age, sexe, "chat")
        self.couleur = couleur

    def miauler(self):
        print(f"{self.nom} miaule : Miaaouuu !")

    def reproduire(self, autre_animal):
        bebe = super().reproduire(autre_animal)
        if bebe:
            return Chat(bebe.nom, 0, bebe.sexe, self.couleur)
        return None
    
    def __str__(self) -> str:
        animal_str = Animal.__str__(self)
        return f"{animal_str}, couleur : {self.couleur}"


class Compagnon():
    def __init__(self, proprietaire) -> None:
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")


class AnimalDomestique(Animal, Compagnon):
    domes_img = """
   O     /\\_/\\
  /|\\   ( o.o )
  / \\    > ^ <
"""
    def __init__(self, nom, age, espece,sexe,  proprietaire):
        # Appel aux deux parents
        Animal.__init__(self, nom, age, sexe, espece)
        Compagnon.__init__(self, proprietaire)

    def __str__(self):
        animal_str = Animal.__str__(self)
        return f"{animal_str}, propriétaire: {self.proprietaire}"

# Test    
print(Chien.chien_img)
un_chien = Chien("Fido", 5, "M", "Golden Retrieve")
un_chien2 = Chien("Roa", 4, "F", "Rottweiler")
un_chien.manger()
un_chien.aboyer()
un_chien.dormir()
print(un_chien)

bebe = un_chien.reproduire(un_chien2)
print(f"\nBébé chien : {bebe}\n")

# Test    
print(Chat.chat_img)
un_chat = Chat("Bob", 2, "M", "orange")
un_chat2 = Chat("Fleur", 4, "F", "noir")
un_chat.miauler()
un_chat.manger()
un_chat.miauler()
print(un_chat)

bebe = un_chat.reproduire(un_chat2)
print(f"\nBébé chat : {bebe}\n")

# Test
print(AnimalDomestique.domes_img)
animal_dom = AnimalDomestique("Achile", 7, "chat", "M", "Mathieu")
animal_dom.manger()   # Hérité de Animal: Buddy mange
animal_dom.jouer()    # Hérité de Compagnon: Je joue avec Alice
print(animal_dom)     # Animal: Buddy, âge: 4 ans, propriétaire: Alice