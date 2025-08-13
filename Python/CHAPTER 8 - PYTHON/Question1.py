class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks should be a list

    def average(self):
        total = 0
        for value in self.marks:
            total += value
        print(f"Hi {self.name}, your average is", total / len(self.marks))


# Creating students with list of marks
s1 = Student("Abhishek", [97, 85, 90])
s2 = Student("Abhisheka", [88, 92, 95])
s3 = Student("Abhishekl", [75, 80, 78])

# Printing names
print(s1.name)
print(s2.name)
print(s3.name)

# Calling average for each
s1.average()
s2.average()
s3.average()
