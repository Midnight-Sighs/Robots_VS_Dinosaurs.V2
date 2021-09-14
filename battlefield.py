from fleet import Fleet
from herd import Herd
from validation import Validation

class Battlefield:
    def __init__(self):
        self.validation = Validation()
        self.fleet = Fleet()
        self.herd = Herd()
        self.d = 0  #dinosaur death counter
        self.r = 0  #robot death counter
        self.player_fleet = False
        self.player_herd = False
        self.player_name = ""
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to our feature battle of Dinosaurs vs Robots!  We have beings from across the galaxy that have prepared teams for you to battle with!  Today, we have the Roombers supplying fleets of modified (and enlarged!) Roombas!  From the planet Brontosoreei II, we have herds of dinosaurs for you to choose from!")
        self.player_name = input("Tell us, master commander, what would you like to be referred to as today?  You don't have to use a name.  You could be whoever or whatever you wish today!  ")
        if self.player_name == "Smelly Cheese" or self.player_name == "smelly cheese":
            print(" Really?? Smelly Cheese is best on toast!!")
        else:
            print("Your name is " + self.player_name+".  Huh.  Interesting...\n")
        self.choose_lists()

    def choose_lists(self):
        print("Alright, " + self.player_name + ".  Are you betting the Roombas will take the gold?  Or do you put your money on the dinosaurs of Brontosoreei II?")
        list_choice = self.validation.valid_1_2("Please type a 1 for robots and a 2 for dinosaurs.  ")
        if list_choice == "1": #(player = fleet, computer = herd)
            self.player_fleet = True
            self.fleet.active_fleet.append(self.fleet.choose_fleet_type())
            self.fleet.equip_fleet_weapons()
            self.herd.active_herd = self.herd.dino_balanced
            print("We here like the idea of Roombas sucking up debris and firing it at unsuspecting dinos!  Roombas should go first! Sorry, dinos!\n\n")
            self.battle_flow()
        if list_choice == "2": #(player = herd, computer = fleet)
            self.player_herd = True
            self.herd.active_herd.append(self.herd.choose_herd_type())
            self.fleet.active_fleet=self.fleet.robot_balanced
            self.fleet.equip_computer_fleet_weapons()
            print("We here like the idea of dinosaurs gnawing on the Roombas, so we think dinosaurs should go first!  Sorry, Roombas!\n\n")
            self.battle_flow()
    
    def choose_active_creatures(self):
        if self.player_herd == True:
            self.herd.choose_active_dinosaur()
            self.fleet.assign_computer_robot()
        if self.player_fleet == True:
            self.fleet.choose_active_robot()
            self.herd.assign_computer_dinosaur()

    def battle_flow(self):
        while self.r <3 and self.d <3:
            if self.player_herd == True:
                self.herd_true_turn_order()
            if self.player_fleet == True:
                self.fleet_true_turn_order()
        if self.player_herd == True and self.r == 3:
            print("You have defeated all of the Roombas and you are victorious!! \nRAWWWR")
        if self.player_herd == True and self.d == 3:
            print("Those Roombas have defeated you! \nYou lose!")
        if self.player_fleet == True and self.d == 3:
            print("Your team of Roombas have eviscerated the dinosaurs! \nCongratulations!")
        if self.player_fleet == True and self.r == 3:
            print("The dinosaurs have torn your robots apart.  \nYou lose.")

    def player_dinosaur_attack_phase(self):
        a_or_d = self.validation.valid_1_2("Would you like your dinosaur to attack(1) or defend?(1)  ")
        if a_or_d == "1":
            self.herd.active_dino.pick_dinosaur_attack(self.fleet.active_robot)
        if a_or_d == "2":
            self.herd.active_dino.dinosaur_defend()

    def player_robot_attack_phase(self):
        a_or_d = self.validation.valid_1_2("Would you like your robot to 1. attack or 2. defend?  ")
        if a_or_d == "1":
            self.fleet.active_robot.robot_attack(self.herd.active_dino)
        if a_or_d == "2":
            self.fleet.active_robot.robot_defend()

    def computer_robot_attack_phase(self):
        if self.fleet.active_robot.battery_charge <= 20:
            self.fleet.active_robot.robot_defend()
        else:
            self.fleet.active_robot.robot_attack(self.herd.active_dino)

    def computer_dinosaur_attack_phase(self):
        if self.herd.active_dino.stamina <=20:
            self.herd.active_dino.dinosaur_defend()
        else:
            self.herd.active_dino.dinosaur_attack(self.fleet.active_robot)

    def herd_true_turn_order(self):
        self.herd.choose_active_dinosaur()
        self.fleet.assign_computer_robot()
        self.player_dinosaur_attack_phase()
        print(f"You have done: {self.herd.active_dino.damage} damage to your enemies hit points!\n")
        if self.fleet.active_robot.hp <=0:
            print("\nA roomba has been desimated by your dinosaur!")
            self.r+=1
            if self.r == 3:
                return
        print("Now it's your opponent's turn!")
        self.computer_robot_attack_phase()
        print(f"Their roomba has hit you for: {self.fleet.active_robot.damage} damage.\n")
        if self.herd.active_dino.hp <=0:
            print("\nOne of your dinosaurs has fallen! NOO!")
            self.d+=1
            if self.d == 3:
                return
        self.herd.active_dino.bonus_defense = 0
        self.fleet.active_robot.bonus_defense = 0

    def fleet_true_turn_order(self):
        self.fleet.choose_active_robot()
        self.herd.assign_computer_dinosaur()
        self.player_robot_attack_phase()
        print(f"You have done: {self.fleet.active_robot.damage} damage to your opponent's Robot!\n")
        if self.herd.active_dino.hp<=0:
            print("\nOne of your Roombas blew a dinosaur away!")
            self.d+=1
            if self.d == 3:
                return
        print("Now it's your opponent's turn.")
        self.computer_dinosaur_attack_phase()
        print(f"They have done {self.herd.active_dino.damage} damage to you.\n")
        if self.fleet.active_robot.hp<=0:
            print("\nOne of your Roombas has fallen! OH NO!!")
            self.r+=1
            if self.r == 3:
                return
        self.herd.active_dino.bonus_defense = 0
        self.fleet.active_robot.bonus_defense = 0

        