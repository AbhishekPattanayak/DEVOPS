# Write a function to find the factrorial of n
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):  #Last value is ignored the range will be from 1 to 5
        print(i)
        fact *=i
    print(fact)  #Collects all the inputs and prints outside the loop

cal_fact(5)  #Called fucn