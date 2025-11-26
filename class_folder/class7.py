# class FileManager:
# A custom context manager to handle file operations

class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode= mode
        self.file = None
    def __enter__(self):
        # Open the file and return the file object
        self.file = open(self.filename, self.mode)
        print(f"Opened file {self.filename} in {self.mode} mode.")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        # Close the file
        if self.file:
            self.file.close()
            print(f"Closed file {self.filename}.")
        # Handle exceptions if any
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception, id needed
    
# USing the custome manager
if __name__ == "__main__": # Ensures this code runs only when the script is executed directly
    with FileManager('example.txt', 'w') as f:
        f.write("Hello, World!")
    with FileManager('example.txt', 'r') as f:
        content = f.read()
        print(f"File content: {content}")
# Output:
# Opened file example.txt in w mode.
# Closed file example.txt.
# Opened file example.txt in r mode.
# File content: Hello, World!
# Closed file example.txt.
# In this example, the `FileManager` class is a custom context manager that handles file
# operations. It opens a file when entering the context and ensures that the file is closed
# when exiting the context, even if an exception occurs. This is useful for managing resources
# like file handling in a clean and efficient manner.
