import statistics


def find_standart_deviation(lista):
    return round(statistics.stdev(lista), 2)


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    resultado = find_standart_deviation(lista)
    print(resultado)
