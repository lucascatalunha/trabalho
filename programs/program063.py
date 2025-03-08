def soma_pares_matriz(matriz):
    return sum(n for linha in matriz for n in linha if n % 2 == 0)


if __name__ == "__main__":
    print(soma_pares_matriz([[1, 2], [3, 4], [5, 6, 8]]))
