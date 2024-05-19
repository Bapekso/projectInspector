from checkPrivateKeyFull import chechKey
from checkCoding import checkCodingScriptsFull
from download import get_variables, get_functions

def problems(file_path):
    try:
        functions = get_functions(file_path)
        variables = get_variables(file_path)
        listOfProblems = []
        listOfProblems += chechKey(variables)
        listOfProblems += checkCodingScriptsFull(functions, variables)

        if not listOfProblems:
            return 'code is good'
        else:
            return listOfProblems
    except Exception as e:
        return [f'Błąd: {str(e)}']
