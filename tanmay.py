data =("Avengers: Doomsday", (18-12-2026, "USA" ), ["Action", "Adventure", "Sci-Fi"])
name, (releasedate, country), genre = data
# Change Action into Avengers: Doomsday
genre[0] = data[0]
print(genre) # ['Avengers: Doomsday', 'Adventure', 'Sci-Fi']
print(f"Movie Name: {name}")
print(f"Releasedate: {releasedate}")
print(f"Genre: {genre}")

# Unpacking with * astrisk in function arguments
def print_names(*names):
    for name in names:
        print(name)
print_names(["Tanmay",21], ["Ankita",23], ["Rohan",21])

#combining list
list1 = [1, 2, 3, 4, 5]
list2 = [3,9,12,15]
combined_list = [*list1, *list2]
sorted_combined_list = sorted(combined_list)
# Make uniques values remopve duplicates from combined_list ?
print(combined_list)
print(sorted_combined_list)

# Unpacking with dictionaries
dict1 = {'a': 1, 'b': 2} # Disctionary write in key value pair
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)

#swapping variables
a = 5
b = 10
a, b = b, a
print(f"a: {a}, b: {b}")
#testing