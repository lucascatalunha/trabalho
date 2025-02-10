def correct_sentence(sentence: str) -> str:
    x = sentence[0].upper()
    if sentence[(len(sentence) - 1)] != ".":
        sentence += "."
    b = sentence[1:]
    return x + b


if __name__ == "__main__":
    a = input("Escreva uma frase: ")
    output = correct_sentence(a)
    print(output)
