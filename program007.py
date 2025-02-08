def double_number(number: int) -> int:
    return number*2


try:
    inputnum = input(
        'Escreva um numero: ')
    print(double_number(inputnum))
except ValueError:
    print('Escreva um número por favor.')
