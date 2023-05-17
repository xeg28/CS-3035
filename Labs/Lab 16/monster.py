class Monster:
    # Constructor initializes the instance fields name and size
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    # Method that takes a string location and returns a string 
    def attack(self, location):
        print(self.name + " attacks " + location)

    # Returns a string if the object is printed
    def __str__(self):
        return self.name + " is a monster that is " + str(self.size) + " ft tall." 
    
    # Overrides the == operator and returns a boolean 
    def __eq__(self, other):
        if self.name == other.name and self.size == other.size:
            return True
        return False
    # Overrides the + operator and returns a Monster instance
    def __add__(self, other):
        return Monster(self.name+other.name, self.size + other.size)

# demonstarting the constructor      
monster1 = Monster("Godzilla", 355)
monster2 = Monster("King Kong", 50)
monster3 = Monster("King Kong", 50)

# demonstrating the attack function
monster1.attack("London")
monster2.attack("New York")

#demonstrating the __str__ function
print()
print(monster1)
print(monster2)

#demonstrating the __eq__ function
print()
print("monster1 equals monster2:", monster1==monster2)
print("monster2 equals monster3:", monster2==monster3)

# demonstrating the __add__ functions
print()
monster4 = monster1+monster2
print("monster4:",monster4)
   



