#WAP to check if a list contains a palinfdrome elements

list1 = [1,2,3,2,1]
list2 = [1, "abc", "abc", 1]

list3 = list1.copy()
list3.reverse()

print(list3)

if(list1 == list3):
    print("list is a palindrome")
else:
    print("list is not a palindrome")

