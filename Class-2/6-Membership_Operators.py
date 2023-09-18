"""
Member in:      ' in '
Member not in:  ' not in '
---* Membership_Operators execution result: True/False. It is used to string data. *---
"""


str1 = "Bangladesh"
str2 = "desh"
str3 = "Desh"

num1 = '25'
num2 = '5'
num3 = '4'

# Member in: 'in'
print(str2 in str1) # True
print(str3 in str1) # Flase

print(num2 in num1) # True
print(num3 in num1) # False


# Member not in: 'not in'
print(str2  not in str1) # Flase
print(str3  not in str1) # True

print(num2 not in num1) # Flase
print(num3 not in num1) # True

