f = open("CHAPTER 7 - PYTHON\demo.txt", "r")  #Given the path for the file with read mode

line1 = f.readline()  #Returns the file to the data variable, you can also specify the number of characters you want to read
line2= f.readline()
print(line1)
print(line2)

print(type(line1))  #Printing the type of the dat

f.close()  #Closing the file
