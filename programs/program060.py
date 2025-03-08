def modify_tuple(tupla, elemento):
    return tupla + (elemento,)


if __name__ == "__main__":
    print(modify_tuple((1, 2, 3), 4))
