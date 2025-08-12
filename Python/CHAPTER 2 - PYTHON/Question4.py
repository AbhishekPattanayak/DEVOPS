#Write a program in python to find the greatest of the three numbers

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the first number:"))
num3 = int(input("Enter the first number:"))

if(num1 > num2 and num1 > num3):
    print("Number1 is greatest")
elif(num2 > num1 and num2 > num3):
    print("Number2 is greatest")
elif(num3 > num1 and num3 > num2):
    print("Number3 is greatest")
else:
    print("Number isnt valid")