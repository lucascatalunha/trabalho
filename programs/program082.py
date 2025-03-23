

# 13. Remover vogais
def remover_vogais(texto):
    return "".join([char for char in texto if char.lower() not in "aeiou"])
