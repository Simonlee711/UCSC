#lab 10
#practicing classes, objects, getters and setters

#Write a code snippet that creates a superclass Tree and two subclasses:
#NurseryTree and ProtectedTree in the following way:

class Tree:
    def __init__(self, age, species):
        self.age = age
        self.species = species
    def set_species(self):
        self.species = species
    def set_age(self):
        self.age = age
    def get_species(self):
        return self.species
    def get_age(self):
        return self.age
    def get_info(self):
        return (("age", str(self.age)), ("species", self.species))
    

class NurseryTree:
    def __init__(self, age, species, cultivar, price):
        self.age = age
        self.species = species
        self.cultivar = cultivar
        self.price = price
    def set_name(self):
        self.species = species
    def set_age(self):
        self.age = age
    def set_cultivar(self):
        self.cultivar = cultivar
    def set_price(self):
        self.price = price
    def get_species(self):
        return self.species
    def get_age(self):
        return self.age
    def get_cultivar(self):
        return self.cultivar
    def get_price(self):
        return self.price
    def get_info(self):
        return (("age", str(self.age)), ("species", self.species),("cultivar", self.cultivar),("price", self.price))

 

class ProtectedTree:
    def __init__(self, age, species, location):
        self.age = age
        self.species = species
        self.location = location
    def set_species(self):
        self.name = species
    def set_age(self):
        self.age = age
    def set_location(self):
        self.location = location
    def get_species(self):
        return self.species
    def get_age(self):
        return self.age
    def get_location(self):
        return self.location
    def get_info(self):
        return (("age", str(self.age)), ("species", self.species),("location", self.location))
    

def print_info(info) :
    for i in info :
        if "age" == i[0]:
            print (f"This tree is { i[1] } years old.")
        elif "species" == i[0]:
            print (f"This tree belongs to { i[1] } species.")
        elif "location" == i[0]:
            print (f"This tree is located in { i[1] }.")
        elif "cultivar" == i[0]:
            print (f"This is { i[1] }.")
        elif "price" == i[0]:
            print (f"This tree costs { i[1] } dollars.")
    print()

# main program
pine = Tree(80, "Pinus radiata")
sequoia = ProtectedTree(1650, "Sequoiadendron giganteum", \
                         "Kings Canyon National Park")
apple = NurseryTree( 4, "Malus domestica", "Golden Delicious", 99.95)

for tree in [pine, sequoia, apple] :
                 print_info(tree.get_info())
