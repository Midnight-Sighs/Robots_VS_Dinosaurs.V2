from dinosaur import Dinosaur
from validation import Validation

class Herd:
    def __init__(self):
        self.valid = Validation()
        self.dino_balanced = [
            Dinosaur("squish","Ceolophysis","Squish",80,15,0 ),
            Dinosaur("basic", "Dilophosaurus","Spite", 100, 10, 5),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 5,10)
        ]
        self.dino_squish = [
            Dinosaur("squish","Ceolophysis","Squish",80,15,0 ),
            Dinosaur("squish","Ceolophysis","Squeeze",80,15,0 ),
            Dinosaur("basic", "Dilophosaurus","Spite", 100, 10, 5)
        ]
        self.dino_tank = [
            Dinosaur("basic", "Dilophosaurus", "Spite", 100, 10, 5),
            Dinosaur("tank", "Allosaurus", "Frankie", 120, 5, 10),
            Dinosaur("tank", "Allosaurus", "Freaky", 120, 5, 10)
        ]
        self.active_herd = []
        self.active_dino = None
        

    def choose_herd_type(self):
        print("\nHello!  We from planet Brontosoreei II have a voraaaacious selection of dinosaurs for you to WRECK HAVOC!  We have a list with three of our most popular dino types!  We have a group for you who strike fear in the hearts of opponents with a single ROAR!  And those who don't look as terrifying...but certainly are.  \n")
        herd_choice = self.valid.valid_to_3("If you would like the balanced list, type 1.  For tanks, type 2.  For squishy Dinos, type 3.\n")
        if herd_choice == "1":
            self.active_herd = self.dino_balanced
        if herd_choice == "2":
            self.active_herd = self.dino_tank
        if herd_choice == "3":
            self.active_herd = self.dino_squish

    def display_dino_list(self):
        print("Your current dinosaurs and their current stats are as follows: ")
        i = 0
        j = 1
        while i < len(self.active_herd):
           print(f" Dino {j} -- Name: {self.active_herd[i].name} -- Hit Points: {self.active_herd[i].hp} -- Stamina: {self.active_herd[i].stamina} -- Bonus Attack Damage: {self.active_herd[i].attack}")
           i+=1
           j+=1

    def choose_active_dinosaur(self):
        self.display_dino_list()
        dino_choice = self.valid.valid_to_3("Which of your dinosaurs would you like to activate for this turn?  Please enter their numeric representation.  ")
        if dino_choice == "1":
            if self.active_herd[0].hp >0:
                self.active_dino = self.active_herd[0]
                print("You have selected", self.active_dino.name)
            else:
                print("That dinosaur was BLOWN away by those debris cannons!  Please select another\n")
                self.choose_active_dinosaur()
        if dino_choice == "2":
            if self.active_herd[1].hp >0:
                self.active_dino = self.active_herd[1]
                print("You have selected", self.active_dino.name)
            else:
                print("That poor dinosaur had his limbs sucked off and he suffered a horrible death.  Please select another one.\n")
                self.choose_active_dinosaur()
        if dino_choice == "3":
            if self.active_herd[2].hp >0:
                self.active_dino = self.active_herd[2]
                print("You have selected", self.active_dino.name)
            else:
                print("That dinosaur has been suckered by the Roombas...into death!\n")
                self.choose_active_dinosaur()

    def assign_computer_dinosaur(self):
        if self.active_herd[0].hp>0:
                self.active_dino = self.active_herd[0]
        elif self.active_herd[1].hp>0:
            self.active_dino = self.active_herd[1]
        else:
            self.active_dino = self.active_herd[2]