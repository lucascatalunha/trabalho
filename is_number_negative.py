
def is_number_negative(number: int) -> bool:
    if number < 0:
        return True

    else:
        return False


try:
    pessoa = int(input('Digite um número: '))

    output = is_number_negative(pessoa)
    print(pessoa)
    print(output)

except ValueError:
    print('Digite um número por favor.')
