import re


def sum_of_digits_between_two_numbers(texto):
    return re.sub(r"[^a-zA-Z0-9 ]", "", texto)


if __name__ == "__main__":
    entrada = "Hello@ World#!*."
    saida = sum_of_digits_between_two_numbers(entrada)
    print(saida)
