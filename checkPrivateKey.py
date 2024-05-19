import re

def checkIfIsKey(variables):
    n = 0
    for var in variables:
        if 'generate_private_key' in var:
            return var
        elif n + 1 == len(variables):
            return False
        n += 1

def checkIfInKeyEverything(variables):
    key = checkIfIsKey(variables)
    needList = ['public_exponent', 'key_size', 'backend']

    whatNeedYet = []

    for i in needList:
        if i not in key:
            whatNeedYet.append(i)

    if whatNeedYet != []:
        return whatNeedYet
    else:
        return False

def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True


def checkIfpublic_exponent(variables):
    key = checkIfIsKey(variables)

    pattern = r'public_exponent=(\d+)'
    match = re.search(pattern, key)

    public_exponent = match.group(1)
    return czy_pierwsza(int(public_exponent))

def checkIfkey_size(variables):
    key = checkIfIsKey(variables)

    pattern = r'key_size=(\d+)'
    match = re.search(pattern, key)

    key_size = int(match.group(1))

    if key_size in [1024, 2048, 3072, 4096, 8192 ]:
        if key_size == 1024:
            return 'Zwiększ liczbę bitów'
        else:
            return True
    else:
        return 'Zła liczba bitów'

def checkIfbackend(variables):
    key = checkIfIsKey(variables)

    pattern = r'backend=(\w+)'
    match = re.search(pattern, key)

    if match is not None:
        backend = match.group(1)
        if backend != 'default_backend':
            return False








