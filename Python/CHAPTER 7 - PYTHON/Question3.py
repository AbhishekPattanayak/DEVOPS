#Search if the word "Learning" exists in the file or not
with open("CHAPTER 7 - PYTHON\sample.txt", "r") as f:
    data = f.read()
    word = "llearning"
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")