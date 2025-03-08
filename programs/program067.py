def soma_dois_menores(lista):
    return sum(sorted(lista)[:2])


if __name__ == "__main__":
    print(soma_dois_menores([10, 15, 5, 8, 20]))
