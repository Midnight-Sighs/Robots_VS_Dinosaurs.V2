from weapon import Weapon
import random
from validation import Validation

def random_int(min, max):
    return random.randint(min, max)

class Robot:
    def __init__(self, type, model, name, hp, armor, attack):
        self.valid = Validation()
        self.type = type
        self.model = model
        self.name = name
        self.hp = hp
        self.weapon = Weapon("Super Sucker", 25,30, "The sucking power on that Roomba is so strong, a dino limb is stuck! OUCH!")
        self.armor = armor
        self.attack = attack
        self.battery_charge = 60
        self.bonus_defense = 0
        self.damage = 0
        self.total_damge = 0

    def robot_attack(self):
        if self.battery_charge <= 10+self.weapon.battery_cost:
            print("Your robot does not have enough Battery Charge to initiate the attack.  It must defend instead.")
            self.robot_defend()
            return
        else:
            self.damage = self.weapon.attack +self.attack
            self.battery_charge -= (10 + self.weapon.battery_cost)
            print(self.weapon.flavor_text)

    def apply_robot_damage(self, dinosaur):
        self.total_damage = self.damage - (dinosaur.scales + dinosaur.bonus_defense)
        if self.total_damage >0:
            dinosaur.hp -= self.total_damage
        else: 
            self.total_damage = 0

    def robot_defend(self):
        self.battery_charge += 30
        self.bonus_defense = 10
        self.total_damage = 0

    basic_equippable_weapons = [
                Weapon("Debris Blaster", 10, 15, "That little blaster may look like an energy weapon, but it fires debris at the dinosaur! Hurts more than you would expect!"),
                Weapon("Debris Sucker", 15, 20, "While your average Roomba sucks up dander and dust, these Roombas have the ability to suck the scales clean off those dinosaurs!"),
                Weapon("Boosted Signal", 5, 10, "With a little bit of boost, the Roomba can do some more damage for a low battery cost!")
    ]

    squish_equippable_weapons = [
                Weapon("Super Sucker", 20,25,"The sucking power on that Roomba is so strong, a dino limb is stuck! OUCH!"), 
                Weapon("Debris Cannon", 25,30, "The Roomba sucks up all the debris in the immediate area and fires it at the dinosaurs! OOF!"),
                Weapon("Ultra Sonic Speed Boost", 15,15, "With the speed that only certain Roombas can attain, their ability to hit quick leads to many dangerous hits!")
    ]

    tank_equipable_weapons = [
                Weapon("Super Sucker", 20,25,"The sucking power on that Roomba is so strong, a dino limb is stuck! OUCH!"), 
                Weapon("Debris Cannon", 25,30, "The Roomba sucks up all the debris in the immediate area and fires it at the dinosaurs! OOF!"),
                Weapon("Towering Fall", 10, 15, "Only the largest of Roombas can threaten an enemy with falling on them...")
    ]
    
    def equip_weapon(self):
        print(f"\nYou must choose what weapons you would like to equip to your robot for the duration of this battle.  You will be unable to choose again once you've made your choice.\nYou are equipping a weapon for {self.name}")
        if self.type == "basic":
            self.equip_weapon_choice(self.basic_equippable_weapons)
        if self.type == "squish":
            self.equip_weapon_choice(self.squish_equippable_weapons)
        if self.type == "tank":
            self.equip_weapon_choice(self.tank_equipable_weapons)

    def equip_weapon_choice(self, weapon_list):
        print("You may equip the following weapons:")
        self.weapon.display_weapon_options(weapon_list)
        user_input = self.valid.valid_int("Please enter the numeric value for the weapon you want to equip  ", len(weapon_list))
        i = user_input -1
        self.weapon = self.basic_equippable_weapons[i]

    def equip_computer_weapons(self):
        if self.type == "basic":
            i = random_int(0, len(self.basic_equippable_weapons)-1)
            self.weapon = self.basic_equippable_weapons[i]
        if self.type == "squish":
            i = random_int(0, len(self.squish_equippable_weapons)-1)
            self.weapon = self.squish_equippable_weapons[i]
        if self.type == "tank":
            i = random_int(0, len(self.tank_equipable_weapons)-1)
            self.weapon = self.tank_equipable_weapons[i]

    def equip_random_weapon(self):
        i = random_int(0, 3)
        self.weapon = self.equippable_weapons[i]

    def flux_shield(self):
        i = random_int(5, 10)
        self.shield = i
        return i