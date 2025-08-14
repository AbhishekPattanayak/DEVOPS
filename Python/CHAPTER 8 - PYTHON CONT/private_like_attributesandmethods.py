class account:
    def __init__(self, account_no, acc_pass):
        self.account_no = account_no
        self.acc_pass = acc_pass

acc1 = account("12345", "abcde")  #So the information should not be directly passed outside the class

print(acc1.account_no)  
print(acc1.acc_pass)


#Private attributes and methods are meant to be used only within the class and are not accessible from outside the class. 


#You can place __ ahead of the method

#You can place __ ahead of the attributes

class Person:
    __name = "anonymous"

    def __hello(self, name):
        print("Hello Person !")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())