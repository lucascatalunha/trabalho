def discount_received(number: int, discount: int) -> int:
    return number - discount


if __name__ == "__main__":
    try:
        inputnum = int(input("Escreva um número: "))
        inputdiscount = int(input("Escreva os disconto, (apenas o número ex: 50): "))
        print(discount_received(inputnum, inputdiscount))
    except ValueError:
        print("Escreva um número por favor.")
