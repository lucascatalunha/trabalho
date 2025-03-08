def first_last_index(lista, elemento):
    if elemento not in lista:
        return None
    primeiro = lista.index(elemento)
    ultimo = len(lista) - 1 - lista[::-1].index(elemento)
    return (primeiro, ultimo)


if __name__ == "__main__":
    lista_teste = [1, 2, 3, 2, 4, 2, 5]
    resultado = first_last_index(lista_teste, 2)
    print(resultado)
