#Print the multiplication table of a number n 

n = int(input("Enter the value that you want:"))
for i in range(10):  #Always n-1, or else you can iterate
    i +=1
    print(n*i)

