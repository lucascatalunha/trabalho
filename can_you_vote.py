
def can_you_vote(input1: int) -> bool:
    if input1 >= 16:
        return True
    else:
        return False


try:
    pessoa = int(input('Digite sua idade: '))

    output = can_you_vote(pessoa)
    print(output)

except ValueError:
    print('Digite um número por favor.')
