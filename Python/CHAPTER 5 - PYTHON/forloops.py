list = [1,2,3,4]

for element in list:  #You can have any keyword which will specify the elemnts
    print(element)     #in is a reserve keyword 

for item in list:
    print(item)

for subject in list:
    print(subject)
else:
    print("END")


string = "Abhishek"  #Traversal through string

for ch in string:
    print(ch)


str = "ApnaCollege"

for ch in str:
    if(ch == 'o'):
        print("O found")
        break
    print(ch)
