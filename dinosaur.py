from robot import random_int
from attack import Attack

class Dinosaur:
    def __init__(self, type, breed, name, hp, attack, scales):
        self.type = type
        self.breed = breed
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = 100
        self.scales = scales
        self.bonus_defense = 0
        self.damage = 0
    
    possible_attacks = [Attack("Claws", 20, "Your dinosaur swipes at a Roomba!  Those claws are SHHHHEEEEAAARP"),
                    Attack("Bite", 25, "Your dinosaur gnaws on a Roomba!"),
                    Attack("Spit", 15, "Your dinosaur just spit! Yeech!  It does burn, though!")]

    def dinosaur_attack(self, robot):
        if self.stamina <= 10:
            print("Your dinosaur does not have enough stamina to attack.  You must defend this turn and restore some.")
            self.dinosaur_defend()
            return
        else:
            i = random_int(0, 2)
            self.damage = (self.attack + self.possible_attacks[i].attack) - (robot.armor + robot.flux_shield() + robot.bonus_defense)
            robot.hp -= self.damage
            self.stamina -= 20
            print(self.possible_attacks[i].flavor_text)

    def dinosaur_defend(self):
        self.stamina += 30
        self.bonus_defense += 10