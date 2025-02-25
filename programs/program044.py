def adding_list_items(lista):
    if len(lista) < 2:
        return "A lista precisa ter pelo menos dois elementos."
    return lista[1] + lista[-2]


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    resultado = adding_list_items(lista)
    print(resultado)  # Saída: 6
