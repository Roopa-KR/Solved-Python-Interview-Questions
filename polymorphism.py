class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives on road")

class Boat(Vehicle):
    def move(self):
        print("Boat sails on water")

class Airplane(Vehicle):
    def move(self):
        print("Airplane flies in air")

vehicles = [Car(), Boat(), Airplane()]

for v in vehicles:
    v.move()