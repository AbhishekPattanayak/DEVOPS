#Write a program to find the sum of the fisrt n numbers using while

n = int(input("Print the sum of the n numbers specified:"))


sum = 0

i = 1

while i < n:
    sum = sum + i
    i +=1

print(sum)