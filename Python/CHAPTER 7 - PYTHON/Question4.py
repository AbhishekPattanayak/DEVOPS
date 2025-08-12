# Write a function to find in which line of the file does the word "Learning" fisrt. Print -1 if word not found
word = "Learning" 
data = "True"
line_no = 1
with open("CHAPTER 7 - PYTHON\sample.txt", "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(line_no)
        line_no += 1
