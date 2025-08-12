#Search for a number x in the tuple using loop 

x = int(input("Enter the number you want to search in the tuple:"))

tup = (1,4,9,16,25,36,49,64,81,100)

for items in tup:
    if (items == x):
        print("Item found at index")
        break
    else:
        print("Item not found")