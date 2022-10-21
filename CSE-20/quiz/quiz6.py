# Quiz 6
# 1) write code for a class Spaceship

class Spaceship :
    def __init__(self, name, size) :
        self.name = name
        self.size = size
    def set_name(self):
        self.name = name
    def set_size(self):
        self.size = size
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def go(self,speed) :
        self.speed = speed
        print ("The speed of " + self.name + " is set to " + str(self.speed) + "!")
    def shoot (self,name) :
        print (ship2.name + " shoots at " + ship1.name + "!")
    def stop(self) :
        print (ship2.name + " stops!")


# main program

ship1 = Spaceship ("Galaxy", 5)
ship2 = Spaceship("Warriors",0)
ship1speed = ship1.go(100)
ship2speed = ship2.go(200)
ship2.shoot(ship1)
ship1.stop()


# 2) Fix a Program
# program code

class Monster :
    def __init__(self, name) :
        self.name = name
    def set_name(self):
        self.name = name
    def get_name(self):
        return self.name
    def attack (self) :
        print (self.name + ": Grr...")
    def sleep (self) :
        print (self.name + ": Zzz...")
    def greet(self) :
        print (monster2.name + ": Hello, " + monster1.name + "!")

# main program

# make a monster named "Frosty"
monster1 = Monster("Frosty")

# make Frosty sleep
monster1.sleep()

# make Frosty attack
monster1.attack()

# make another monster named "Candy"
monster2 = Monster("Candy")

# make Candy greet Frosty
monster2.greet()

#code runs perfectly
