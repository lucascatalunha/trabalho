def soma_digitos(inicio, fim):
    return sum(int(d) for n in range(inicio, fim + 1) for d in str(n))


if __name__ == "__main__":
    print(soma_digitos(10, 15))
