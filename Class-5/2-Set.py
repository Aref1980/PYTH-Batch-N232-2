"""
>> Set <<
- Unordered, Un-indexed
- Duplicate  not allow
- Unchangeable but remove item and add item

"""
myset = set()
print(type(myset)) # <class 'set'>

myset2 = {}
print(type(myset2)) # <class 'dict'>

# Duplicate  not allow

myset2 = {1, 2, 3, 4, 5, 1}
print(myset2) # {1, 2, 3, 4, 5}

"""
# Unordered, Un-indexed
print(myset2[2]) # TypeError

# Unchangeable 
myset2[2]= 8
print(myset2) # TypeError

"""

# Add item

myset2.add("Python")
print(myset2) # {1, 2, 3, 4, 5, 'Python'}

# Update data

myset2.update([9, 5, 8])
print(myset2) # {1, 2, 3, 4, 5, 8, 9, 'Python'}

# Discard item, If the data is not available no Error

myset2.discard(8)
print(myset2) # {1, 2, 3, 4, 5, 'Python', 9}

myset2.discard(800)
print(myset2) # {1, 2, 3, 4, 5, 'Python', 9}

# Remove item
myset2.remove(5)
print(myset2) # {1, 2, 3, 4, 'Python', 9}

myset2.remove(50)
print(myset2) # KeyError, When data os not available then Error

