f = open("CHAPTER 7 - PYTHON\demo.txt", "r")  #Given the path for the file with read mode

data = f.read(5)  #Returns the file to the data variable, you can also specify the number of characters you want to read

print(data)

print(type(data))  #Printing the type of the dat

f.close()  #Closing the file


