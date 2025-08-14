class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  #This allows us to access the function of the parent class.

car2 = ToyotaCar("Prius", "Electric")
print(car2.type)

print(car2.start())