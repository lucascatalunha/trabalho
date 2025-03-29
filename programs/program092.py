def indice_primeira_vogal(texto):
    for i, char in enumerate(texto):
        if char.lower() in "aeiou":
            return i
    return -1
