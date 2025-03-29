def embaralhar_indices(texto):
    pares = texto[::2]
    impares = texto[1::2]
    return pares + impares
