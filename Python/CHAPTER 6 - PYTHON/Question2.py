#Write a function to print the elements of a list in a single line\

my_list = []

def list_line(lst):
    for i in range(5):
        element = input("Enter an element: ")
        lst.append(element)
    return lst

print(list_line(my_list))