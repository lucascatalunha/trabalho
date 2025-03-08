import re


def remover_caracteres_especiais(texto):
    return re.sub(r"[^a-zA-Z0-9 ]", "", texto)


if __name__ == "__main__":
    entrada = "Hello@ World#!*."
    saida = remover_caracteres_especiais(entrada)
    print(saida)
