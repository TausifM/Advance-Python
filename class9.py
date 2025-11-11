# while yield

# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line
# immediately after the loop in the program is executed.

# In this example, the condition for while will be True as long as the counter variable (count) is less than 3.

# yield: Execution Pause and Value Return: When the yield statement is encountered within a while loop, the function's execution is temporarily suspended. 
# The value specified after yield is returned to the caller.

# Resumption: The next time a value is requested from the generator (e.g., by calling next() on the generator object or iterating over it in a for loop), 
# the function resumes execution from the point immediately after the yield statement. The while loop continues its iteration, potentially leading to another yield.
# Iteration until Exhausted: This process continues until the while loop condition becomes false or the generator function explicitly returns or raises a 
# StopIteration exception. yield allows the function to produce a series of values over time, rather than computing them all at once and sending them back.

count = 0
while count < 3:
    count = count + 1
    print("Hello Geek", count)


def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current # Yield the current value and pause execution
        current += 1 # Increment current to avoid infinite loop
        

# Example usage:
counter = count_up_to(5)
for num in counter:
    print(num)  # Output: 1 2 3 4 5