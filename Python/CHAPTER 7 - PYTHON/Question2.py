#Write a function that replaces all the occurences of "Java" with "Python"

with open("sample.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")

print(new_data)

with open("sample.txt", "w") as f:
    f.write(new_data)