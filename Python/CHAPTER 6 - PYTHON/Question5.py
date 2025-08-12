# Code to print even and odd 

b = int(input("The value of the number:"))

def odd_even(num):
    if num %2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    return num

odd_even(b)
