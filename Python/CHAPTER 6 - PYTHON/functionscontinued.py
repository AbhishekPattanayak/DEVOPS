#WAP to check if a is greater than the two numbers if yes then print the average of the three numbers


a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))

def average_value(a,b,c):
    if (a > b and a > c):
        average = (a+b+c)/3
        return average  # If you want to return a value inside a if else block then the return shouldd be inside the incdenttation of the if else block
    
print(average_value(a,b,c))