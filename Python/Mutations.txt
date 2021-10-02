def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = "".join(string)
    return string


###############################################################

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
