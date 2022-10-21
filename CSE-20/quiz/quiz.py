# program code

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
