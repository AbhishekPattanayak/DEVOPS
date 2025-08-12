# i = 1

# while i <= 5:
#     print(i)
#     if (i ==3):
#         break  # Breaks the loop when the condition matches
#     i += 1

i = 1

while i <= 5:
    if (i ==3):
        i +=1
        continue  # skip
    print(i)
    i += 1  #Always increment the i before the continue or else this will cause an infinite loop 

print("End of the Looop")