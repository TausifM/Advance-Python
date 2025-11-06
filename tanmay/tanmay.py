data =("Avengers: Doomsday", (18-12-2026, "USA" ), ["Action", "Adventure", "Sci-Fi"])
name, (release_date, country), genre = data    
print(f"Movie Name: {name}")
print(f"release_date: {release_date}")
print(f"genre: {genre}")

# Unpacking with *
def print_names(*names):
    for name in names:
        print(name)
print_names(["Tanmay",21], ["Ankita",23], ["Rohan",21])
per
#combining list
list1 = [1, 2, 3, 4, 5]
list2 = [3,9,12,15]
combined_list = [*list1, *list2]
sorted_combined_list = sorted(combined_list)
print(combined_list)
print(sorted_combined_list)

# Unpacking with dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)

#swapping variables
a = 5
b = 10
a, b = b, a
print(f"a: {a}, b: {b}")
#testing

#demonstrate exec
def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""
    local_scope = {}
    exec(code, {}, local_scope)
    greeting = local_scope['greet']("Tanmay")
    print(greeting)
demonstrate_exec()

#demonstrate eval
def demonstrate_eval():
    expression = input("Enter a mathematical expression to evaluate: ")
    result = eval(expression)
    print(f"Result of the expression '{expression}' is: {result}")
demonstrate_eval()

#demonstrate_safe_eval
def demonstrate_safe_eval():
    expression = input("Enter a mathematical expression: ")
    variables = {'x': 10, 'y': 5}
    result = eval(expression, {}, variables)
    print(f"Result of the expression '{expression}'is: {result}")
demonstrate_safe_eval()