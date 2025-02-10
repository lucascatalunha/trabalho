def string_concatenation(str1: str, str2: str) -> str:
    return str1 + str2


if __name__ == "__main__":
    try:
        inputstr1 = str(input("Escreva um palavra: "))
        inputstr2 = str(input("Escreva outra palavra: "))
        print(string_concatenation(inputstr1, inputstr2))
    except ValueError:
        print("Escreva uma palavra por favor.")
