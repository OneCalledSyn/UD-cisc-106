import random

class Cat:
    def __init__(self, name, num_lives):
        self.name = name
        self.num_lives = num_lives
    
    def die(self):
        forms_of_death = ["Drowned", "Eaten", "Electrocuted", "Clawed", "Infected", "Poisoned"]
        self.num_lives -= 1
        print("{0} died from being {1}. {2} lives left.".format(
            self.name, random.choice(forms_of_death), self.num_lives))
        while (self.num_lives > 0):
            dinner.die()    
            
dinner = Cat("Fluffy", 9)           

dinner.die()