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
        self.bonus_defense = 0

    def robot_attack(self, dinosaur):
        dinosaur.hp -= (self.weapon.attack +self.attack - dinosaur.scales)
        self.battery_charge -= 10

    def robot_defend(self):
        self.battery_charge += 20
        self.bonus_defense = 10

    equippable_weapons = [Weapon("Super Sucker", 20, ("The sucking power on that Roomba is so strong, a dino limb is stuck! OUCH!")), 
                        Weapon("Debris Cannon", 25, "The Roomba sucks up all the debris in the immediate area and fires it at the dinosaurs! OOF!"),
                        Weapon("Debris Blaster", 5, "That little blaster may look like an energy weapon, but it fires debris at the dinosaur! Hurts more than you would expect!"),
                        Weapon("Debris Sucker", 15, "While your average Roomba sucks up dander and dust, these Roombas have the ability to suck the scales clean off those dinosaurs!")]

    def equip_weapon(self):
        i = random_int(0, 3)
        self.weapon = self.equippable_weapons[i]

    def flux_shield(self):
        i = random_int(5, 15)
        self.shield = i
        return i