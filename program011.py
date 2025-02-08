def correct_sentence(sentence: str) -> str:
    x = sentence[0].upper()
    if sentence[(len(sentence) - 1)] != ".":
        sentence += "."
    b = sentence.replace(sentence[0], "")
    return x + b


a = input("Escreva uma frase: ")
output = correct_sentence(a)
print(output)
