from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.d = 0  #dinosaur death counter
        self.r = 0  #robot death counter
        self.player_fleet = False
        self.player_herd = False
        self.player_name = self.display_welcome()

    def display_welcome(self):
        print("Welcome to our feature battle of Dinosaurs vs Robots!  We have beings from across the galaxy that have prepared teams for you to battle with!  Today, we have the Roombers supplying fleets of modified (and enlarged!) Roombas!  From the planet Brontosoreei II, we have herds of dinosaurs for you to choose from!")
        self.player_name = input("Tell us, master commander, what would you like to be referred to as today?  You don't have to use a name.  You could be whoever or whatever you wish today!  ")
        if self.player_name == "Smelly Cheese" or self.player_name == "smelly cheese":
            print(" Really?? Smelly Cheese is best on toast!!")
        else:
            print("Your name is " + self.player_name+".  Huh.  Interesting...")
        self.choose_lists()

    def choose_lists(self):
        print("Alright," + self.player_name + ".  Are you betting the Roombas will take the gold?  Or do you put your money on the dinosaurs of Brontosoreei II?")
        list_choice = input("Please type a 1 for robots and a 2 for dinosaurs.")
        if list_choice == "1": #(player = fleet, computer = herd)
            self.player_fleet = True
            self.fleet.active_fleet.append(self.fleet.choose_fleet_type())
            self.fleet.equip_fleet_weapons()
            self.herd.active_herd = self.herd.dino_balanced
            print("We here like the idea of Roombas sucking up debris and firing it at unsuspecting dinos!  Roombas should go first! Sorry, dinos!")
            self.battle_flow()
        if list_choice == "2": #(player = herd, computer = fleet)
            self.player_herd = True
            self.herd.active_herd.append(self.herd.choose_herd_type())
            self.fleet.active_fleet=self.fleet.robot_balanced
            print("We here like the idea of dinosaurs gnawing on the Roombas, so we think dinosaurs should go first!  Sorry, Roombas!")
            self.battle_flow()
    
    def battle_flow(self):
        while self.r <3 or self.d <3:
            if self.player_herd == True:
                self.herd_true_turn_order()
            if self.player_fleet == True:
                self.fleet_true_turn_order()
        if self.player_herd == True and self.r == 3:
            print("You have defeated all of the Roombas and you are victorious!! RAWWWR")
        if self.player_herd == True and self.d == 3:
            print("Those Roombas have defeated you! You lose!")
        if self.player_fleet == True and self.d == 3:
            print("Your team of Roombas have eviscerated the dinosaurs! Congratulations!")
        if self.player_fleet == True and self.r == 3:
            print("The dinosaurs have torn your robots apart.  You lose.")

    def choose_active_dino(self):
        self.herd.display_dino_list()
        dino_choice = input("Which of your dinosaurs would you like to activate for this turn?  Please enter their numeric representation.")
        if dino_choice == "1":
            if self.herd.active_herd[0].hp >0:
                self.herd.active_dino = self.herd.active_herd[0]
                print("You have selected", self.herd.active_dino.name)
            else:
                print("That dinosaur was BLOWN away by those debris cannons!  Please select another")
                self.choose_active_dino()
        if dino_choice == "2":
            if self.herd.active_herd[1].hp >0:
                self.herd.active_dino = self.herd.active_herd[1]
                print("You have selected", self.herd.active_dino.name)
            else:
                print("That poor dinosaur had his limbs sucked off and he suffered a horrible death.  Please select another one.")
                self.choose_active_dino()
        if dino_choice == "3":
            if self.herd.active_herd[2].hp >0:
                self.herd.active_dino = self.herd.active_herd[2]
                print("You have selected", self.herd.active_dino.name)
            else:
                print("That dinosaur has been suckered by the Roombas...into death!")
        #assigning computer's active robot
        if self.fleet.active_fleet[0].hp>0:
            self.fleet.active_robot = self.fleet.active_fleet[0]
        elif self.fleet.active_fleet[1].hp>0:
            self.fleet.active_robot = self.fleet.active_fleet[1]
        else:
            self.fleet.active_robot = self.fleet.active_fleet[2]

    def choose_active_robot(self):
        self.fleet.display_robots_in_list()
        robot_choice = input("Which of your robots would you like to activate this turn?  Please enter the numerical representation.  ")
        if robot_choice == "1":
            if self.fleet.active_fleet[0].hp >0:
                self.fleet.active_robot = self.fleet.active_fleet[0]
                print("You have selected", self.fleet.active_robot.name)
            else:
                print("That Roomba has been destroyed, please select another one.")
                self.choose_active_robot()
        if robot_choice == "2":
            if self.fleet.active_fleet[1].hp>0:
                self.fleet.active_robot = self.fleet.active_fleet[1]
                print("You have selected", self.fleet.active_robot.name)
            else:
                print("The Roomba you've attempted to select is dead.  You can't reactivate him!")
                self.choose_active_robot()
        if robot_choice == "3":
            if self.fleet.active_fleet[2].hp>0:
                self.fleet.active_robot = self.fleet.active_fleet[2]
                print("You have selected", self.fleet.active_robot.name)
            else:
                print("That Roomba has been brutally shattered by a dinosaur, please select another!")
                self.choose_active_robot()
        #setting computer active dino
        if self.herd.active_herd[0].hp>0:
            self.herd.active_dino = self.herd.active_herd[0]
        elif self.herd.active_herd[1].hp>0:
            self.herd.active_dino = self.herd.active_herd[1]
        else:
            self.herd.active_dino = self.herd.active_herd[2]

    def player_dinosaur_attack_phase(self):
        a_or_d = input("Would you like your dinosaur to 1. attack or 2. defend?")
        if a_or_d == "1":
            self.herd.active_dino.dinosaur_attack(self.fleet.active_robot)
        if a_or_d == "2":
            self.herd.active_dino.dinosaur_defend()

    def player_robot_attack_phase(self):
        a_or_d = input("Would you like your robot to 1. attack or 2. defend?")
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
        self.choose_active_dino()
        self.player_dinosaur_attack_phase()
        print(f"You have done: {self.herd.active_dino.damage} damage to your enemies hit points!")
        if self.fleet.active_robot.hp <=0:
            print("A roomba has been desimated by your dinosaur!")
            self.r+=1
            if self.r == 3:
                return
        print("Now it's your opponent's turn!")
        self.computer_robot_attack_phase()
        print(f"Their roomba has hit you for: {self.fleet.active_robot.damage} damage.")
        if self.herd.active_dino.hp <=0:
            print("One of your dinosaurs has fallen! NOO!")
            self.d+=1
            if self.d == 3:
                return
        self.herd.active_dino.bonus_defense = 0
        self.fleet.active_robot.bonus_defense = 0

    def fleet_true_turn_order(self):
        self.choose_active_robot()
        self.player_robot_attack_phase()
        print(f" You have done: {self.fleet.active_robot.damage} damage to your opponent's Robot!")
        if self.herd.active_dino.hp<=0:
            print("One of your Roombas blew a dinosaur away!")
            self.d+=1
            if self.d == 3:
                return
        print("Now it's your opponent's turn.")
        self.computer_dinosaur_attack_phase()
        print(f"They have done {self.herd.active_dino.damage} damage to you.")
        if self.fleet.active_robot.hp<=0:
            print("One of your Roombas has fallen! OH NO!!")
            self.r+=1
            if self.r == 3:
                return
        self.herd.active_dino.bonus_defense = 0
        self.fleet.active_robot.bonus_defense = 0

        