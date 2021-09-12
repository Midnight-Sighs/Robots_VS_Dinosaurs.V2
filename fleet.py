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

    def display_fleet(self):
        for robot in self.active_fleet:
            print(robot.name)
    
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