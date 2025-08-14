# class person:
#     name = "any"

#     def changeName(self, name):
#         self.name = name

# p1 = person()

# p1.changeName("Rahul Kumar")  #This doesnt change the name variable that was declared in the class person

# print(p1.name)


class person:
    name = "any"

    @classmethod
    def changeName(cls, name): #cls is referring to the class
        cls.name = name  #This directly affects the attributes of the class 

p1 = person()

p1.changeName("Rahul Kumar")  #This doesnt change the name variable that was declared in the class person

print(p1.name)
