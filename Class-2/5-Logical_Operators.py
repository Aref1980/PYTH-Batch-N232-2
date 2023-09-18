"""
    Logical and:-   'and'
    Logical or:-    'or'
    Logical not:-   'not'
---* Logical_Operators execution result: True/False *--
"""
num1 = 5
num2 = 12
num3 = 9
a = True
b = False
c = True
# Logical and:- 'and'
print((num1 < num2) and (num2 < num3)) # False
print(a and c) # True

# Logical or:- 'or'
print((num1 < num2) or (num2 < num3)) # True
print(a or b or c) # True

# Logical not:- 'not'
print(not num1 < num2) # False


