# Unpacking Nested Structures
data = ("Alice", (25, "Engineer"), ["Reading", "Traveling", "Swimming"])
name, (age, profession), [hobbies, travel, swimming] = data
# hobbies = data[1] (25, "Engineer")
# print(hobbies[1]) # R
# print(hobbies[2]) # e
print(f"Name: {name}, Age: {age}, Profession: {profession}, Hobbies: {hobbies}, Travel: {travel}, Swimming: {swimming}")
# Name: Alice, Age: 25, Profession: Engineer, Hobbies: Alice, Travel: Swimming, Swimming: Swimming

# Unpacking with function arguments
def print_names(*names):
    for name in names:
        print(f"Name: {name}")
        
print_names(["Bob", 25], ["Charlie", 30], ["David", 35])

# Name: ['Bob', 25]
# Name: ['Charlie', 30]
# Name: ['David', 35]

# Combining Lists with Unpacking
list1 = [1, 2, 3, 7, 8, 9]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(*list1)  # 1 2 3 7 8 9
sorted_combined = sorted(combined_list)

print(f"Combined List: {combined_list}") # Combined List: [1, 2, 3, 7, 8, 9, 4, 5, 6]
print(f"Sorted Combined List: {sorted_combined}") # Sorted Combined List: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Merging Dictionaries with Unpacking 
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
merged_dict = {**dict1, **dict2}
print(f"Merged Dictionary: {merged_dict}") # Merged Dictionary: {'x': 1, 'y': 3, 'z': 4}
# Note: In case of key conflicts, the value from the latter dictionary is used.

# Swapping Variables
x = 10
y = 20
x, y = y, x
print(f"x: {x}, y: {y}") # x: 20, y: 10