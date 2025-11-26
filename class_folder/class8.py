# class my range
# Python range() function
# Last Updated : 11 Jul, 2025
# The Python range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequences on a sequence of numbers using Python loops.

# for i in range(5):
#     print(i, end=" ")
# print()

# output : 0 1 2 3 4 

# Syntax of Python range() function
# Syntax: range(start, stop, step)

# Parameter :

# start: [ optional ] start value of the sequence
# stop: next value after the end value of the sequence
# step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
# Return : Returns an object that represents a sequence of numbers


# What is the use of the range function in Python
# In simple terms, range() allows the user to generate a series of numbers within a given range. Depending on how many arguments the user is passing to the function, the user can decide where that series of numbers will begin and end, as well as how big the difference will be between one number and the next. Python range() function takes can be initialized in 3 ways.

# range (stop) takes one argument.
# range (start, stop) takes two arguments.
# range (start, stop, step) takes three arguments.

# for i in range(2, 10, 2): # output 2 4 6 8 
#     print(i, end=" ")   

# How to make the function which can use in other files using export ?

    
class MyRange:
    def __init__ (self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """
        The __iter__ method makes this class an iterable
        It Should return an iterator object.
        """
        return self
    def __next__(self):
        """
        The __next__ method defines the iteration behaviour 
        It should return the next item in the sequence or raise StopIteration.
        """
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Example usage:
if __name__ == "__main__":
    my_range = MyRange(1, 5)
    for num in my_range:
        print(num, end=" ")  # Output: 1 2 3 4