from weapon import Weapon
import random

def random_int(min, max):
    return random.randint(min, max)

class Robot:
    def __init__(self, type, model, name, hp, armor, attack):
        self.type = type
        self.model = model
        self.name = name
        self.hp = hp
        self.weapon = Weapon("Super Sucker", 15)
        self.armor = armor
        self.attack = attack
        self.battery_charge = 100

    def robot_attack(self, dinosaur):
        dinosaur.hp -= (self.weapon.attack +self.attack - dinosaur.scales)
        self.battery_charge -= 10

    equippable_weapons = [Weapon("Super Sucker", 20), 
                        Weapon("Debris Cannon", 25),
                        Weapon("Debris Blaster", 5),
                        Weapon("Debris Sucker", 15)]

    def equip_weapon(self):
        i = random_int(0, 3)
        self.weapon = self.equippable_weapons[i]

    def flux_shield(self):
        i = random_int(5, 15)
        self.shield = i
        return i