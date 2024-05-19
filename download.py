import ast

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def get_functions(filename):
    source_code = read_file(filename)
    tree = ast.parse(source_code)
    functions_code = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno - 1
            end_line = node.end_lineno
            func_code = '\n'.join(source_code.splitlines()[start_line:end_line])
            functions_code.append(func_code)
    return functions_code

def get_variables(filename):
    source_code = read_file(filename)
    tree = ast.parse(source_code)
    variables_code = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if node.col_offset == 0:
                variables_code.append(source_code.splitlines()[node.lineno - 1])
    return variables_code


