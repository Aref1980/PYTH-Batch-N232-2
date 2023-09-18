"""
-List store the sequence of various type of data [Integer, floating, string, Boolean, list, etc]
-Dynamically handel list size
-List are ordered
-Element can access by index
-Mutuable type

"""
# 1-> Creating a empty list

lst = []
print(type(lst)) # <class 'list'>

lst1 = list()
print(lst1) # []

# Creating a list of various data

lst = [2, 5.4, "python", [2,4,5], True]
print(lst) # [2, 5.4, "python", [2,4,5], True]
"""
         lst = [2, 5.4, "python", [2,4,5], True]
Index Number = [0,  1,      3,       4,      5]
"""

print(lst[1]) # 5.4

print(lst[-1]) # Ture

print(lst[:3]) # 2, 5.4, Python
print(lst[0:3]) # 2, 5.4, Python

print(lst[3]) # [2,4,5]
print(lst[3][1]) # 4

# 2-> length of list
print(len(lst)) # 5

# 3-> Adding element to a list
lst2 = ['A', 'B', 'D', 'A', 'P']
num = 2000

lst.append(lst2)
print(lst) # [2, 5.4, 'python', [2, 4, 5], True, ['A', 'B', 'D', 'A', 'P']]
lst.append(num)
print(lst) # [2, 5.4, 'python', [2, 4, 5], True, ['A', 'B', 'D', 'A', 'P'], 2000]

lst.extend(lst2)
print(lst) # [2, 5.4, 'python', [2, 4, 5], True, ['A', 'B', 'D', 'A', 'P'], 2000, 'A', 'B', 'D', 'A', 'P']

# 4-> Remove from list

lst2.remove('A') # Remove first 'A' from lst2
print(lst2) # ['B', 'D', 'A', 'P']

print(lst2[0]) # B

print(lst) # [2, 5.4, 'python', [2, 4, 5], True, ['B', 'D', 'A'], 2000, 'A', 'B', 'D', 'A', 'P']

lst2.pop() # Remove last variable from lst2
print(lst2) # ['B', 'D', 'A']

print(lst) # [2, 5.4, 'python', [2, 4, 5], True, ['B', 'D', 'A'], 2000, 'A', 'B', 'D', 'A', 'P']

lst.pop(2)
print(lst) # [2, 5.4, [2, 4, 5], True, ['B', 'D', 'A'], 2000, 'A', 'B', 'D', 'A', 'P']

lst.clear()
print(lst) # []