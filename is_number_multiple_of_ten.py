def is_number_multiple_of_ten(input1: int):
    verification = (input1 % 10) == 0
    return verification


input1 = input("Escreva um número: ")
try:
    input1 = int(input1)

    output1 = is_number_multiple_of_ten(input1)

    print(output1)
except ValueError as error:
    print("Error de transformação de valor")
    print(error)
except Exception as error:
    print("Error geral")
    print(error)
