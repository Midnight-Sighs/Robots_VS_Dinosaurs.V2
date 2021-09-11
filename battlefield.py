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
        print("Your name is " + self.player_name+".  Huh.  Interesting...")
        self.choose_lists()

    def choose_lists(self):
        print("Alright," + self.player_name + ".  Are you betting the Roombas will take the gold?  Or do you put your money on the dinosaurs of Brontosoreei II?")
        list_choice = input("Please type a 1 for robots and a 2 for dinosaurs.")
        if list_choice == "1":
            #player = Fleet()
            self.fleet.active_fleet.append(self.fleet.choose_fleet_type())
            self.fleet.equip_fleet_weapons()
            self.herd.active_herd = self.herd.dino_balanced
            self.battle()
        if list_choice == "2":
            #player = self.herd
            self.herd.active_herd = self.herd.choose_herd_type()
            #computer = self.fleet
            self.battle()

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