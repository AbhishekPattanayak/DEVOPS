# 1. Single Inheritance
# 2. Multi-level inheritance
# 3. Multiple Inheritance


#Single-level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")

# print(car1.start())  #Car1 is the object of the "ToyotaCar", which doesnt have the start() function but still it works because ToyotaCar class has inherited the properties of the Car class

#Mulilevel inheritance
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

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

#Multiple inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):  #Class C  inherited the properties of class A and Class B
     varC ="Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
