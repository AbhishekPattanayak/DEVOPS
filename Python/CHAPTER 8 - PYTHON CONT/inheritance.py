class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")

print(car1.start())  #Car1 is the object of the "ToyotaCar", which doesnt have the start() function but still it works because ToyotaCar class has inherited the properties of the Car class

