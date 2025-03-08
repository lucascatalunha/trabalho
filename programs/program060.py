def adicionar_elemento_tupla(tupla, elemento):
    return tupla + (elemento,)


if __name__ == "__main__":
    print(adicionar_elemento_tupla((1, 2, 3), 4))
