# Decorators for class methods
# What is a decorator in Python?
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
# This is useful for cross-cutting concerns like logging, authentication, and caching.
# Decorators can be applied to class methods as well.
# Here's an example:
# Why use decorators with class methods?
# Decorators can help in modifying or enhancing the behavior of methods in a clean and readable way.
# Why decorators are useful in python
# Decorators provide a way to wrap additional functionality around existing code, promoting code reuse and separation of concerns.
# How to use decorators in python?
# You can define a decorator function and then apply it to a class method using the `@decorator_name` syntax.


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the method.")
        result = func(*args, **kwargs)
        print("After calling the method.")
        return result
    return wrapper

class MyClass:
    @my_decorator
    def my_method(self, x):
        print(f"Inside the method with argument: {x}")
        return x * 2
# Usage
obj = MyClass()
result = obj.my_method(5)
print(f"Result: {result}")
# Output:
# Before calling the method.
# Inside the method with argument: 5
# After calling the method.
# Result: 10
# In this example, the `my_decorator` function is defined to wrap around the `my_method` of `MyClass`.
# When `my_method` is called, the decorator adds behavior before and after the method execution.
# This demonstrates how decorators can be effectively used with class methods in Python.