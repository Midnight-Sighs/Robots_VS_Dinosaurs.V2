from robot import Robot


class Fleet:
    def __init__(self):
        self.robot_balanced = [
            Robot("squish","Mega Roomba ++", "Art", 80, 0, 5),
            Robot("basic", "Roomba", "Bob", 100, 5, 0),
            Robot("tank", "Armored Roomba +", "Patrick", 120, 10, 0),
        ]
        self.robot_squish = [
            Robot("squish","Mega Roomba ++", "Art", 80, 0, 5),
            Robot("squish","Mega Roomba ++", "Mary", 80, 0, 5),
            Robot("basic", "Roomba", "Bob", 100, 5, 0)
        ]
        self.robot_tank = [
            Robot("basic", "Roomba", "Bob", 100, 5, 0),
            Robot("tank", "Armored Roomba +", "Patrick", 120, 10, 0),
            Robot("tank","Armored Roomba +", "Anne", 120, 10, 0)
        ]
        self.active_fleet = []
        self.active_robot = None
    
    def equip_fleet_weapons(self):
        for robot in self.active_fleet:
            Robot.equip_weapon(robot)

    def choose_fleet_type(self):
        print("Hello!  We from planet Roomba would like to offer a sampling of a variety or different types of Roombas!  You can pick our balanced list that includes three different types of Roombas!  Or, if you prefer survivability, we have some heavy-duty Roombas available in our tank group.  Lastly, we have some Roombas that are built to take some damage!  They're just a bit more fragile.")
        fleet_choice = input("If you would like the balanced list, type 1.  For tanks, type 2.  For squishy Roombas, type 3.")
        if fleet_choice == "1":
            self.active_fleet = self.robot_balanced
        if fleet_choice == "2":
            self.active_fleet = self.robot_tank
        if fleet_choice == "3":
            self.active_fleet = self.robot_squish

    def display_robots_in_list(self):
        print("Your current robots and their stats are as follows: ")
        i = 0
        j = 1
        while i < len(self.active_fleet):
            print (f"Robot {j} -- Name: {self.active_fleet[i].name} -- Hit Points: {self.active_fleet[i].hp} -- Battery Charge: {self.active_fleet[i].battery_charge} -- Bonus Attack Damage: {self.active_fleet[i].attack}")
            i+=1
            j+=1