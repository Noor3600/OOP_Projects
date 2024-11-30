# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method.")

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())