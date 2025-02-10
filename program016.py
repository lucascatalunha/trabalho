def string_concatenation(str1: str, str2: str) -> str:
    return str1 + str2


try:
    inputstr1 = str(input("Escreva um número: "))
    inputstr2 = str(input("Escreva os disconto, (apenas o número ex: 50): "))
    print(string_concatenation(inputstr1, inputstr2))
except ValueError:
    print("Escreva uma palavra por favor.")
