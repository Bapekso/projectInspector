from checkPrivateKey import checkIfIsKey, checkIfInKeyEverything, checkIfpublic_exponent, checkIfkey_size, checkIfbackend

def chechKey(variables):
    listOfProblems = []
    if checkIfIsKey(variables) is False:
        listOfProblems.append('-' * 20)
        listOfProblems.append('Nieposiadzasz klucza prywatnego.')
        listOfProblems.append('-' * 20)
        listOfProblems.append(' ')

    else:
        whatWeNeed = checkIfInKeyEverything(variables)
        if whatWeNeed is False:

            if checkIfpublic_exponent(variables):
                print('')
            else:
                listOfProblems.append('-' * 20)
                listOfProblems.append("'public_exponent' w kluczu prywatnym musi być liczbą pierwszą")
                listOfProblems.append('-' * 20)
                listOfProblems.append(' ')

            if checkIfkey_size(variables) == 'Zła liczba bitów':
                listOfProblems.append('-' * 20)
                listOfProblems.append("'key_size' w kluczu prywatnym ma złą liczbę bitów, zmień na np 2048")
                listOfProblems.append('-' * 20)
                listOfProblems.append(' ')
            elif checkIfkey_size(variables) == 'Zwiększ liczbę bitów':
                listOfProblems.append('-' * 20)
                listOfProblems.append("'key_size' w kluczu prywatnym ma zamałą liczbę bitów, zmień na np 2048")
                listOfProblems.append('-' * 20)
                listOfProblems.append(' ')

        else:
            listOfProblems.append('-' * 20)
            listOfProblems.append('W kluczu prywatnym')
            for i in whatWeNeed:
                listOfProblems.append(f'We need: {i}')
            listOfProblems.append('-' * 20)
            listOfProblems.append(' ')

        if checkIfbackend(variables) is False:
            listOfProblems.append('-' * 20)
            listOfProblems.append("'backend' w kluczu prywatnym powinien być 'default_backend()'")
            listOfProblems.append('-' * 20)
            listOfProblems.append(' ')




    return listOfProblems


