def remover_n_esimo(texto, n):
    return texto[:n] + texto[n + 1 :] if 0 <= n < len(texto) else texto
