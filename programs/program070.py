def list_xor(lista):
    from functools import reduce

    return reduce(lambda x, y: x ^ y, lista)
