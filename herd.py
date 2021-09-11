from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_balanced = [
            Dinosaur("squish","Ceolophysis","Squish",80,0,10 ),
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 5, 0),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 10, 5)
        ]
        self.dino_squish = [
            Dinosaur("squish","Ceolophysis","Squish",80,0,10 ),
            Dinosaur("squish","Ceolophysis","Squeeze",80,0,10 ),
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 5, 0)
        ]
        self.dino_tank = [
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 5, 0),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 10, 5),
            Dinosaur("tank", "Allosaurus", "Freaky", 120, 10, 5)
        ]
        self.active_herd = []
        

    def choose_herd_type(self):
        print("Hello!  We from planet Brontosoreei II have a voraaaacious selection of dinosaurs for you to WRECK HAVOC!  We have a list with three of our most popular dino types!  We have a group for you who strike fear in the hearts of opponents with a single ROAR!  And those who don't look as terrifying...but certainly are.  ")
        herd_choice = input("If you would like the balanced list, type 1.  For tanks, type 2.  For squishy Roombas, type 3.")
        if herd_choice == "1":
            self.active_fleet = self.dino_balanced
        if herd_choice == "2":
            self.active_fleet = self.dino_tank
        if herd_choice == "3":
            self.active_fleet = self.dino_squish