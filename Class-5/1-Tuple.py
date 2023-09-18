"""
>> List <<

- Store [Integer, Floating, String, Boolean, List, etc.]
- Dynamically handle list size.
- Ordered.
- Access by index
- Mutuable type.
- Changeable

>> Tuple <<
- Access by index
- Ordered
- Duplicate allow
- Unchangeable
"""

# Creating empty Tuple

tpl = ()
print(type(tpl))

tpl1 = tuple()
print(type(tpl1))

tpl1 =( "Python", True, [1, 2, 3, 4], 7, 9.5)
print(tpl1)

print(tpl1[:2])
print(tpl1[0:2])
print(tpl1[-2])
print(tpl1[2][2])

# Update Value
"""
tpl1[3] = "Python"
print(tpl1) # TypeError, because  Tuple don't support updating
"""
lst1 =["Python", True, [1, 2, 3, 4], 7, 9.5]
print(lst1) #['Python', True, [1, 2, 3, 4], 7, 9.5]
lst1[1] = "False"
print(lst1) # ['Python', 'False', [1, 2, 3, 4], 7, 9.5]


# Concat

tpl2 = (2, 3, 1, 5)
tpl3= ('Python', 9, 3, 1)
tpl4 = tpl2 + tpl3
print(tpl4)

lst2 = [2, 3, 1, 5]
lst3= ['Python', 9, 3, 1]
lst4 = lst2 + lst3
print(lst4)