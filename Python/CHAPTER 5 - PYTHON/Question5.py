# Search a number x in this tuple using loop

tup = (1,4,9,16,36,49,64,16,100)
x = int(input("Enter the number that you want to search:"))

i = 0

while i < len(tup):
    if tup[i] == x:
        print(x, "The index where the element found is:" ,i)
    i += 1
