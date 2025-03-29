def primeira_unica(texto):
    from collections import Counter

    contagem = Counter(texto)
    for char in texto:
        if contagem[char] == 1:
            return char
    return ""
