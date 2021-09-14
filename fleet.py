from robot import Robot
from validation import Validation


class Fleet:
    def __init__(self):
        self.valid = Validation()
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
            robot.equip_weapon()

    def equip_computer_fleet_weapons(self):
        for robot in self.active_fleet:
            robot.equip_computer_weapons()

    def choose_fleet_type(self):
        print("Hello!  We from planet Roomba would like to offer a sampling of a variety or different types of Roombas!  You can pick our balanced list that includes three different types of Roombas!  Or, if you prefer survivability, we have some heavy-duty Roombas available in our tank group.  Lastly, we have some Roombas that are built to take some damage!  They're just a bit more fragile.\n")
        fleet_choice = self.valid.valid_to_3("If you would like the balanced list, type 1.  For tanks, type 2.  For squishy Roombas, type 3.  ")
        if fleet_choice == "1":
            self.active_fleet = self.robot_balanced
        if fleet_choice == "2":
            self.active_fleet = self.robot_tank
        if fleet_choice == "3":
            self.active_fleet = self.robot_squish

    def choose_active_robot(self):
        self.display_robots_in_list()
        robot_choice = input("Which of your robots would you like to activate this turn?  Please enter the numerical representation.  ")
        if robot_choice == "1":
            if self.active_fleet[0].hp >0:
                self.active_robot = self.active_fleet[0]
                print("You have selected", self.active_robot.name)
            else:
                print("That Roomba has been destroyed, please select another one.\n")
                self.choose_active_robot()
        if robot_choice == "2":
            if self.active_fleet[1].hp>0:
                self.active_robot = self.active_fleet[1]
                print("You have selected", self.active_robot.name)
            else:
                print("The Roomba you've attempted to select is dead.  You can't reactivate him!\n")
                self.choose_active_robot()
        if robot_choice == "3":
            if self.active_fleet[2].hp>0:
                self.active_robot = self.active_fleet[2]
                print("You have selected", self.active_robot.name)
            else:
                print("That Roomba has been brutally shattered by a dinosaur, please select another!\n")
                self.choose_active_robot()

    def assign_computer_robot(self):
        if self.active_fleet[0].hp>0:
            self.active_robot = self.active_fleet[0]
        elif self.active_fleet[1].hp>0:
            self.active_robot = self.active_fleet[1]
        else:
            self.active_robot = self.active_fleet[2]

    def display_robots_in_list(self):
        print("Your current robots and their stats are as follows: ")
        i = 0
        j = 1
        while i < len(self.active_fleet):
            print (f"Robot {j} -- Name: {self.active_fleet[i].name} -- Hit Points: {self.active_fleet[i].hp} -- Battery Charge: {self.active_fleet[i].battery_charge} -- Bonus Attack Damage: {self.active_fleet[i].attack} -- Weapon: {self.active_fleet[i].weapon.name}")
            i+=1
            j+=1