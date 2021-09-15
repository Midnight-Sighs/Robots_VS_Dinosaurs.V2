from robot import random_int
from attack import Attack
from validation import Validation

class Dinosaur:
    def __init__(self, type, breed, name, hp, attack, scales):
        self.validation = Validation()
        self.type = type
        self.breed = breed
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = 100
        self.scales = scales
        self.bonus_defense = 0
        self.damage = 0
    
    squish_attacks = [
            Attack("Hoard", 25,20, "\nThe dinosaur calls to his friends and they gang up on the Roomba!"),
            Attack("Claws", 10,10, "\nThe dinosaur swipes at a Roomba!  Those claws are SHHHHEEEEAAARP"),
            Attack("Bite", 15,15, "\nThe dinosaur gnaws on a Roomba!"),
    ]

    basic_attacks = [
            Attack("Bite", 15, 15, "\nThe dinosaur rakes his class across the roomba!"),
            Attack("Claws", 5, 5, "\nThose claws may be sharp, but they're not the sharpest! Or the longest..."),
            Attack("Screech",10,10, "\nThat sounds like a banshee in mourning and the poor Roombas seem to be having some glitches as a result!" )
    ]

    tank_attacks = [
            Attack("Claws", 15, 20, "\nThose dinos may have some sharp claws, but they don't have the best reach for powerful strike!"),
            Attack("Bite", 25,25, "\nThat's one bite I would never want to experience myself!!"),
            Attack("Roar", 10, 15, "\nThat roar is so terrifying even the Roombas can hear it!")
    ]

    def pick_dinosaur_attack(self):
        if self.stamina < 10:
            print("Your dinosaur does not have enough stamina to do any attacks.")
            self.dinosaur_defend()
        else:
            if self.type == "basic":
                self.choose_dinosaur_attack(self.basic_attacks)
            if self.type == "squish":
                self.choose_dinosaur_attack(self.squish_attacks)
            if self.type == "tank":
                self.choose_dinosaur_attack(self.tank_attacks)

    def dinosaur_defend(self):
        self.stamina += 30
        self.bonus_defense += 10

    def display_dinosaur_attacks(self, attack_list):
        i = 0
        j = 1
        for attack in attack_list:
            print(f"Attack {j} {attack_list[i].name} -- Attack Damage: {attack_list[i].attack} -- Stamina Drain: {attack_list[i].stamina_cost}")
            i+=1
            j+=1

    def choose_dinosaur_attack(self, attack_list):
        self.display_dinosaur_attacks(attack_list)
        user_input = self.validation.valid_int("Please enter a number matching the attack you would like to use this turn  ", len(attack_list))
        i = user_input-1
        self.damage = (self.attack + attack_list[i].attack)
        self.stamina -= attack_list[i].stamina_cost
        print(attack_list[i].flavor_text)

    def computer_dinosaur_attack(self, robot):
        if self.stamina < 10:
            self.dinosaur_defend()
            print("Your opponent has used defense on their dinosaur.  ")
        else:
            if self.type == "basic":
                self.apply_computer_dinosaur_damage(self.basic_attacks, robot)
            if self.type == "squish":
                self.apply_computer_dinosaur_damage(self.squish_attacks, robot)
            if self.type == "tank":
                self.apply_computer_dinosaur_damage(self.tank_attacks, robot)

    def apply_computer_dinosaur_damage(self, attack_list, robot):
        i = random_int(0, len(attack_list))
        i -1
        robot.hp -= (self.attack+attack_list[i].attack) - (robot.armor + robot.flux_shield() + robot.bonus_defense)
            
    def apply_dinosaur_damage(self, robot):
        robot.hp -= self.damage - (robot.armor + robot.flux_shield() + robot.bonus_defense)