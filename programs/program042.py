def eliminate_odds(lista):
    return [numero for numero in lista if numero % 2 == 0]


if __name__ == "__main__":
    lista_entrada = [1, 2, 3, 4, 5]
    resultado = eliminate_odds(lista_entrada)
    print(resultado)
