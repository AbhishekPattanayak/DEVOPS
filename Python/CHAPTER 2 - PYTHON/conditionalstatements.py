# age = 21

age = int(input("Enter your age: "))

if(age >= 18):   #Exceutes first if the condition is met then stop execution of the code
    print("You can apply for driver's license")
elif(age <=18):  #Needs an if statement to exist
    print("You cant apply for a driver's license")
else:
    print("You are dead")