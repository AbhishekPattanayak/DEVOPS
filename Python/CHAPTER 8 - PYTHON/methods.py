class student:
    college_name = "ITER"  # This is a class attribute and all the object will get the propert of the class
    name = "Alpita"

    def hello(self):
        print("Hello!")
    #Parameterized constructor
    def __init__(self, fullname , marks):
        self.name = fullname #Object attribute 
        self.marks = marks
        print("Adding new student to the database")

s1 = student("Karan", 97)

print(s1.name, s1.marks)

print(student.college_name)

print(s1.name) #Object attribute > class attribute (When object attribute and class attribute have the same value)

s1.hello()