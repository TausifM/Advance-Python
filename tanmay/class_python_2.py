data= ("Tanmay", (21, "Male"), ["Reading", "Traveling", "Coding"])
name, (age, gender), hobbies = data
hobbies = data[2]
print(f"Name: {name}, age: {age}, Gender: {gender}, Hobbies: {hobbies}")
hobbies[1] = data[2]

def print_info(*names):
    for name in names:
        print(f"Hello, {name}")
print_info("Tanmay", "Sanskruti", "Omkar")

list1 = [2,5,1,7,3]
list2 = [4,8,0,9,6]
combined = [*list1, *list2]
print(combined)
sorted_combined = sorted(combined)
print(sorted_combined)

dict1 = {'a': "Thor", 'b': "Loki"}
dict2 = {'c': "Odin", 'd': "Ironman"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

x= "Man"
y= "Iron"
print(x)
print(y)
x,y = y,x
print(x,y)