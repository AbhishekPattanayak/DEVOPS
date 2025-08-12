age = int(input("Enter the age:"))
#80 is the age limit where the person cant drive 
if(age >= 18):
    if(age >= 80):
        print("The person cant drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")