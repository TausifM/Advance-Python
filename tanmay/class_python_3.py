def demonstrate_exec():
    code = """def greet(name):
        return f'Avengers {name}'"""
    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope['greet']('Assemble'))
demonstrate_exec()

def demonstrate_eval():
    expression = input("Enter a mathematical expression: ")
    result = eval(expression)
    print("Result:", result)
demonstrate_eval()

def demonstrate_safe_eval():
    expression = input("Enter a mathematical expression: ")
    variables = {'x': 10, 'y': 5}
    result = eval(expression, {}, variables)
    print("Result =", result)
demonstrate_eval()