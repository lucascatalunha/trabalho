def split_strings(sentence: str) -> str:
    vogais = "aeiouAEIOU"

    vogais_str = ""
    consoantes_str = ""

    for char in sentence:
        if char in vogais:
            vogais_str += char
        elif char.isalpha():
            consoantes_str += char

    return vogais_str, consoantes_str


entrada = "hello"
vogais, consoantes = split_strings(entrada)
print(vogais)
print(consoantes)
