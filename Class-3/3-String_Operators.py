name = "shahide mostafa mohammad Aref rabbani"

print(name.upper()) # SHAHIDE MOSTAFA MOHAMMAD AREF RABBANI
print(name.lower()) # shahide mostafa mohammad aref rabbani
print(name.capitalize()) # Shahide mostafa mohammad aref rabbani
print(name.title()) # Shahide Mostafa Mohammad Aref Rabbani

print(len(name)) # 37 (length of variable)
# How many "a" in (1-37)
print(name.count("a")) # 7

# How many "a" in (1-15)
print(name.count("a",1,15)) # 3

# How many "a" in (0-6)
print(name.count("a",0,6)) # 1

# How many "a" in (15-37)
print(name.count("a",15,37)) # 4

# Replace
print(name.replace("a","7")) # sh7hide most7f7 moh7mm7d Aref r7bb7ni
