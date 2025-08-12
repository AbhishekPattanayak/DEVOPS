#Create a file "Practice.txt" using python. Add the following data in it

with open("sample.txt", "w") as f:
    data = f.write("Hi everyone\nwe are learning File I/O\nusingJava\nI like programming in java")
    print(data)