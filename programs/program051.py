def diferenca_simetrica(conjunto1, conjunto2):
    return conjunto1 ^ conjunto2


if __name__ == "__main__":
    c1 = {1, 2, 3, 4}
    c2 = {3, 4, 5, 6}
    resultado = diferenca_simetrica(c1, c2)
    print(resultado)
