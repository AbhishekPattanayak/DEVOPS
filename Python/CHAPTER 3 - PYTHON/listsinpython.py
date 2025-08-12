list = [22,23.5,22.2,55.8]

# List is a set of data stored in a single variable -> list[]

print(list)

print(type(list))

print(list[0])  # You can access any index of the list

print(len(list))  # You can print the length of the list


student = ["Abhishek", 28 , "Rourkela"] # You can save various datatypes within a single list

print(student)

student[0] = "Alpita" # Lists are mutable, strings are not

print(student)

print(student[1:len(student)]) #List slicing is also possible

print(student[-3:-1])