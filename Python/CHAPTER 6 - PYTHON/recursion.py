# def show(n):
#     if (n == 0):  #Base case where you are defining when the recursive function to stop
#         return
#     print(n)
#     show(n-1)

# show(5)



#Homework - Understand call stack and recursive function 


def calc_sum(n):
    if (n ==0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)