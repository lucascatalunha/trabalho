def divisible_by_five(input1: int) -> bool:
    verification = (input1 % 5) == 0
    return verification


if __name__ == "__main__":
    input1 = input("Escreva um número: ")
    try:
        input1 = int(input1)

        output1 = divisible_by_five(input1)

        print(output1)
    except ValueError as error:
        print("Error de transformação de valor")
        print(error)
    except Exception as error:
        print("Error geral")
        print(error)
