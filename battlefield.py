from attack import Attack
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
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
            self.fleet.active_fleet.append(self.fleet.choose_fleet_type())
            self.fleet.equip_fleet_weapons()
            self.herd.active_herd = self.herd.dino_balanced
            print("We here like the idea of Roombas sucking up debris and firing it at unsuspecting dinos!  Roombas should go first! Sorry, dinos!")
            
        if list_choice == "2": #(player = herd, computer = fleet)
            self.herd.active_herd.append(self.herd.choose_herd_type())
            self.fleet.active_fleet=self.fleet.robot_balanced
            print("We here like the idea of dinosaurs gnawing on the Roombas, so we think dinosaurs should go first!  Sorry, Roombas!")
            self.choose_active_dino()

    def choose_active_dino(self):
        self.herd.display_dino_list()
        dino_choice = input("Which of your dinosaurs would you like to activate for this turn?  Please enter their numeric representation.")
        if dino_choice == "1":
            self.herd.active_dino = self.herd.active_herd[0]
        if dino_choice == "2":
            self.herd.active_dino = self.herd.active_herd[1]
        if dino_choice == "3":
            self.herd.active_dino = self.herd.active_herd[2]
        print("You have selected", self.herd.active_dino.name)

    def choose_active_robot(self):
        self.fleet.display_robots_in_list()
        robot_choice = input("Which of your robots would you like to activate this turn?  Please enter the numerical representation.  ")

    def battle(self):
        d=0
        r=0
        while r <=2 or d <=2:
            print("The dinosaur gnaws at a Roomba.")
            self.herd.active_herd[d].dinosaur_attack(self.fleet.active_fleet[r])
            print("Roomba HP:", self.fleet.active_fleet[r].hp)
            if self.fleet.active_fleet[r].hp <= 0:
                print("A roomba has violently shattered.")
                r += 1
            if r == 3 and self.fleet.active_fleet[2].hp <= 0:
                print("THE DINOSAURS ARE VICTORIOUS! RAWR!")
                break
            print("The roomba attempts to fire debris at the dinosaur.")
            self.fleet.active_fleet[r].robot_attack(self.herd.active_herd[d])
            print("Dinosaur HP:", self.herd.active_herd[d].hp)
            if self.herd.active_herd[d].hp <= 0:
                print("NOOO!! A dino has fallen!!")
                d +=1
            if d == 3 and self.herd.active_herd[2].hp <= 0:
                print("The roombas are taking over the world.  These don't seem to be the friendly sort.  ")
                break