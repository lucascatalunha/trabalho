# 16. Converter número para lista de dígitos invertida
def converter_reverso(numero):
    return list(map(int, str(numero)[::-1]))
