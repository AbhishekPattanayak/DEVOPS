class student:
    def __init__(self,name):
        self.name = name

s1 = student("Shradha")

print(s1.name)

del s1.name  #Del keword is used to delete the object properties or delete the enire object itself

print(s1.name)