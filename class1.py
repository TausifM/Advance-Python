# Basic variable assignment and unpacking in Python
a,b,c = [1,2,3]
print(f"a: {a}, b: {b}, c: {c}") # a: 1, b: 2, c: 3

# Extended unpacking Iterables
a, *b = [1,2,3,4,5, 6, 7, 8, 9, 10 ]
print(f"a: {a}, b: {b}, c: {c}") # a: 1, b: [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ignoring Values
_, _, c = [1,2,3]
print(f"_" , f"_: {_}, c: {c}") # _: 2, c: 3