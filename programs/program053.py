def primeiros_ultimos_indices(lista, elemento):
    if elemento not in lista:
        return None
    primeiro = lista.index(elemento)
    ultimo = len(lista) - 1 - lista[::-1].index(elemento)
    return (primeiro, ultimo)


if __name__ == "__main__":
    lista_teste = [1, 2, 3, 2, 4, 2, 5]
    resultado = primeiros_ultimos_indices(lista_teste, 2)
    print(resultado)
