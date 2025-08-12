# Write to find the factorial of n 

n = int(input("Enter the number:"))
i = n
fact = 1

while i > 0:
    fact *= i
    i -= 1

print("Factorial:", fact)