# Union
A = {1, 2, 3, 4, 5,}
B = {4, 5, 6, 7, 8, 9}

print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection
print(A.intersection(B)) # {4, 5}
print(A & B) # {4, 5}

# Defference
print(A.difference(B)) # {1, 2, 3}
print(A-B) # {1, 2, 3}

print(B.difference(A)) # {8, 9, 6, 7}
print(B-A) # {8, 9, 6, 7}

print(5 in B) # True
print(5 not in B) # false
