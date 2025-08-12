# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value

dict = {}
   
subject = str(input("Enter the subject"))
marks = int(input("Enter the marks scored"))
dict.update({subject:marks})

print(dict)