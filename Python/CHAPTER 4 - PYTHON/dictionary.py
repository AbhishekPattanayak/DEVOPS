info = {"key" : "value", "name": "Abhishek", "learning": "coding", "marks": [33,44,55]}
#dictionaries can store multiple data types, but the key can not be a list. A tuple can also be a key
print(info)

print(type(info))

print(info["key"]) # This is how the key is called in dictionary

info["key"] = "null"  #assign a new value to the key

print(info)

null_dict = {}  #Declared a empty dictionary

null_dict["name"] = "Abhishek"
print(null_dict)