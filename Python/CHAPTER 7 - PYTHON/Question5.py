#From a file containing numbers separated by comma, print the count of even numbers
count = 0
with open("CHAPTER 7 - PYTHON\practice.txt", "r") as f:
    data = f.read()
    print(data)

nums = data.split(",")

print(nums)

for value in nums:
    if((int(value)) % 2 == 0):
        count +=1

print(count)