marks = int(input("Enter the student's mark:"))

if(marks >= 90):
    print("Student has secured A")
elif(marks>= 80 and marks< 90):
    print("Student has secured B")
elif(marks>=70 and marks <80):
    print("Student has secured C")
elif(marks <70):
    print("Student has secured D")


print("End of conditionals")