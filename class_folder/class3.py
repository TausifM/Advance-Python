def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""
    # Excecute the code string
    local_scope = {}
    exec(code, {}, local_scope)
    # Call the function defined in the executed code
    greeting = local_scope["greet"]("World")
    print(greeting)  # Output: Hello, World!
    
demonstrate_exec()

def demonstrate_eval():
    # Evalaute the expression
    expression = input("Enter a mathematical expression (e.g., 2 + 3 * 4): ")
    result = eval(expression)
    print(f"The result of the expression '{expression}' is: {result}")
    
demonstrate_eval()

def demonstrate_safe_eval():
    # expresssion to be evaluated
    expression  = input("Enter a mathematical expression (e.g., 2 + 3 * 4): ")
    
    # Defined variables for the expression
    variables = {'a': 2, 'b': 3, 'c': 4}

    # Evaluate the expression in the context of the provided variables
    result = eval(expression, {}, variables)
    print(f"The result of the expression '{expression}' is: {result}")

demonstrate_safe_eval()