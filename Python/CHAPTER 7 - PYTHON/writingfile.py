f = open("CHAPTER 7 - PYTHON\demo.txt", "w")  #Given the path for the file with read mode

data = f.write("I want to learn python")

print(data)

f.close()


# #Simple modes

# 1. Read - "r"
# 2. Write - "w"
# 3. Append - "a"

# #Different modes 

# 1. r+ -> read + overwrite (Pointer at the start) -> No truncate
# 2. w+ -> write -> Truncate
# 3. a+ -? append -> pointer at the end -> No truncate
