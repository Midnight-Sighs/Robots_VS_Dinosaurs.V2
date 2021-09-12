from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_balanced = [
            Dinosaur("squish","Ceolophysis","Squish",80,10,0 ),
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 0, 5),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 5,10)
        ]
        self.dino_squish = [
            Dinosaur("squish","Ceolophysis","Squish",80,10,0 ),
            Dinosaur("squish","Ceolophysis","Squeeze",80,10,0 ),
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 0, 5)
        ]
        self.dino_tank = [
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 0, 5),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 5, 10),
            Dinosaur("tank", "Allosaurus", "Freaky", 120, 5, 10)
        ]
        self.active_herd = []
        self.active_dino = None
        

    def choose_herd_type(self):
        print("Hello!  We from planet Brontosoreei II have a voraaaacious selection of dinosaurs for you to WRECK HAVOC!  We have a list with three of our most popular dino types!  We have a group for you who strike fear in the hearts of opponents with a single ROAR!  And those who don't look as terrifying...but certainly are.  ")
        herd_choice = input("If you would like the balanced list, type 1.  For tanks, type 2.  For squishy Dinos, type 3.")
        if herd_choice == "1":
            self.active_herd = self.dino_balanced
        if herd_choice == "2":
            self.active_herd = self.dino_tank
        if herd_choice == "3":
            self.active_herd = self.dino_squish

    def display_dino_list(self):
        print("Your current dinosaurs and their current stats are as follows:")
        i = 0
        j = 1
        while i < len(self.active_herd):
           print(  f" Dino {j} -- Name: {self.active_herd[i].name} -- Hit Points: {self.active_herd[i].hp} -- Stamina: {self.active_herd[i].stamina} -- Bonus Attack Damage: {self.active_herd[1].attack}")
           i+=1
           j+=1