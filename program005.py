def largest_of_two(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    # elif num2 == num1:
    #     return num1
    return num2


try:
    inputnum1 = input('Escreva um número: ')
    inputnum2 = input('Escreva outro número: ')
    print(largest_of_two(inputnum1, inputnum2))
except ValueError:
    print('Escreva um número por favor.')
