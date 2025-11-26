import itertools
# This module provides various utility functions for working with iterators. It includes functions for creating iterators for efficient looping,
# such as count, cycle, repeat, and functions for combining or grouping iterators.

# Example usage of itertools
counter = itertools.count(
    start=10, step=3
) # Infinite counter starting at 10, increasing by 3

print(next(counter))  # Output: 10 # Why next ? because count is infinite iterator
print(next(counter))  # Output: 13
print(next(counter))  # Output: 16
print(next(counter))  # Output: 19

# Cycling through a finite sequence infinitely

cycle = itertools.cycle(['A', 'B', 'C'])
print(next(cycle))  # Output: A
print(next(cycle))  # Output: B
print(next(cycle))  # Output: C
print(next(cycle))  # Output: A Repeats

# Creating combinations of elements
combinations = itertools.combinations(['X', 'Y', 'Z'], 2)
print(list(combinations))  # Output: [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
#Return successive r-length combinations of elements in the iterable. combinations(range(4), 2) --> (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)

# Creating permutations of elements
permutations = itertools.permutations(['1', '2', '3'], 2)
print(list(permutations))  # Output: [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# Return successive r-length permutations of elements in the iterable.permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

# Usage of itertools to group elements
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4)]
data.sort(key=lambda x: x[0])  # Sort data by the first element to ensure grouping works correctly 
# Why lambda ? because we are passing function as key to sort method 
grouped_data = itertools.groupby(data, key=lambda x: x[0])
for key, group in grouped_data:
    print(key, list(group)) 
# Output:
# A [('A', 1), ('A', 3)]
# B [('B', 2), ('B', 4)]

#Usgae of itertools to chain multiple iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
chained = itertools.chain(list1, list2)
print(list(chained))  # Output: [1, 2, 3, 'a', 'b', 'c']
    
# Usgae of itertools all above methods in real world scenario
# Imagine you are processing a large dataset and you want to generate unique pairs of items, cycle
# and count occurrences efficiently without loading everything into memory at once.
data = ['apple', 'banana', 'cherry', 'date']
pair_combinations = itertools.combinations(data, 2)
for pair in pair_combinations:
    print(f"Processing pair: {pair}")
    # Processing pair: ('apple', 'banana')
    # Processing pair: ('apple', 'cherry')
    # Processing pair: ('apple', 'date')
    # Processing pair: ('banana', 'cherry')
    # Processing pair: ('banana', 'date')
    # Processing pair: ('cherry', 'date')
    
counter = itertools.count(1)
for item in data:
    print(f"Item {next(counter)}: {item}")
cycler = itertools.cycle(data)
for _ in range(6):  # Just to demonstrate cycling through first 6 items
    print(f"Cycled item: {next(cycler)}")