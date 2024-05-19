from download import get_functions, get_variables

bad_algorithms = [
    "md5",
    "sha1"
]

def checkCodingScripts(functions, variables):
    for i in functions:
        for j in bad_algorithms:
            if j in i:
                return j
    for i in variables:
        for j in bad_algorithms:
            if j in i:
                return j
    return False

def checkCodingScriptsFull(functions, variables):
    listOfProblems = []
    if checkCodingScripts(functions, variables) == 'md5':
        listOfProblems.append('-' * 20)
        listOfProblems.append('W kodzie masz kodowanie md5. Użyj innego.')
        listOfProblems.append('-' * 20)
        listOfProblems.append(' ')

    elif checkCodingScripts(functions, variables) == 'sha1':
        listOfProblems.append('-' * 20)
        listOfProblems.append('W kodzie masz kodowanie sha1. Użyj innego.')
        listOfProblems.append('-' * 20)
        listOfProblems.append(' ')

    return listOfProblems




