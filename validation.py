class Validation:
    def __init__ (self):
        self.user_input = ""

    def valid_1_2(self, prompt):
        two_ints = False
        while two_ints == False:
            user_input = input(prompt)
            if user_input =="1" or user_input =="2":
                two_ints = True
                return user_input
                
    def valid_to_3(self, prompt):
        three_ints = False
        while three_ints == False:
            user_input = input(prompt)
            if user_input =="1" or user_input =="2" or user_input == "3":
                three_ints = True
                return user_input

    def valid_int(self, prompt, amount):
        integer = False
        while integer == False:
            user_input = int(input(prompt))
            if (isinstance(user_input, int)) and user_input <= amount:
                integer = True
        return user_input