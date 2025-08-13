# class Person:
#     def __init__(self, name, age):
#         self.name = name  # assigning to object
#         self.age = age

# # Creating objects
# p1 = Person("Alice", 25)  #Here init function assigns the value when the object is being created insided the class
# p2 = Person("Bob", 30)

# print(p1.name, p1.age)  # Alice 25
# print(p2.name, p2.age)  # Bob 30


class student:
    college_name = "ITER"  # This is a class attribute and all the object will get the propert of the class
    #Parameterized constructor
    def __init__(self, fullname , marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student to the database")

s1 = student("Karan", 97)

print(s1.name, s1.marks)