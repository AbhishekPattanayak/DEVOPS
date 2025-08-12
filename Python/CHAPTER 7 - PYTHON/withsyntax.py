with open("CHAPTER 7 - PYTHON\demo.txt", "r") as f:
    data = f.read()

print(data)  #With will automatically close the file

with open("CHAPTER 7 - PYTHON\demo.txt","w") as f:
    f.write("New data")
    