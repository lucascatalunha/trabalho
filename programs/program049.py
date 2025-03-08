import re


def remove_special_characters_from_string(texto):
    return re.sub(r"[^a-zA-Z0-9 ]", "", texto)


if __name__ == "__main__":
    entrada = "Hello@ World#!*."
    saida = remove_special_characters_from_string(entrada)
    print(saida)
