def double_number(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    try:
        inputnum = int(input("Escreva um numero: "))
        print(double_number(inputnum))
    except ValueError:
        print("Escreva um número por favor.")
