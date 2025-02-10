def square_number(number: int) -> int:
    return number + 10


try:
    inputnum = int(input("Escreva um numero: "))
    print(square_number(inputnum))
except ValueError:
    print("Escreva um número por favor.")
