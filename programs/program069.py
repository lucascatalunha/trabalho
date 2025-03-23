# 1. Converter string em lista de palavras
def string_para_lista(texto):
    return texto.split()


















# 25. Índice da primeira vogal
def indice_primeira_vogal(texto):
    for i, char in enumerate(texto):
        if char.lower() in "aeiou":
            return i
    return -1