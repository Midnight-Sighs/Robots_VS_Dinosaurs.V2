class Weapon:
    def __init__(self, name, attack, battery_cost, flavor_text):
        self.name = name
        self.attack = attack
        self.battery_cost = battery_cost
        self.flavor_text = flavor_text

    def display_weapon_options(self, weapon_list):
        i = 0
        j = 1
        while i < len(weapon_list):
            print(f"Weapon {j} -- Name: {weapon_list[i].name} -- Damage: {weapon_list[i].attack} -- Battery Drain: {weapon_list[i].battery_cost}")
            i+=1
            j+=1