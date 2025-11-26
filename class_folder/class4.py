# variables annotation and unpacking
name: str = "Alice"
age: int = 30
is_student: bool = False

# Function annotations
def greet(x:str, age: int) -> str: 
    return f"Hello, {x}! You are {age} years old."

print(greet(name, age))

# Showing Annotation
print("\n function annotations:", greet.__annotations__)
print("variable annotations:", __annotations__)
