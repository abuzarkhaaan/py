class Vehicle:
    def general_usage(self):
        print("genreral usage : transportation")
class Car(Vehicle):
    def __init__(self) :
        print("im car")
        self.wheels= 4
        self.has_roof=True

    def specific_usage(self):
        print("usage for family")

class Motorcycle(Vehicle):
    def __init__(self) :
        print("Im a motorcycle")
        self.wheels = 2
        self.has_roof= False

    def specific_usage(self):
        self.general_usage
        print("Specific use : road trip and racing")

m= Motorcycle()
c=Car()
print(issubclass(Car,Motorcycle))