def add_to_number(number: int) -> int:
    return number + 10


if __name__ == "__main__":
    try:
        inputnum = int(input("Escreva um numero: "))
        print(add_to_number(inputnum))
    except ValueError:
        print("Escreva um número por favor.")
