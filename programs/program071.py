# 3. Operação XOR em lista
def xor_lista(lista):
    from functools import reduce
    return reduce(lambda x, y: x ^ y, lista)