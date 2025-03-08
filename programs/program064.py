def palavras_comecam_vogais(frase):
    return [palavra for palavra in frase.split() if palavra[0].lower() in "aeiou"]


if __name__ == "__main__":
    print(palavras_comecam_vogais("These are apple and orange"))
