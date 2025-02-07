

def passfail(a):
    if a < 50:
        return 'Failed'
    else:
        return 'Passed'


try:
    avaliacao = int(input('Digite a nota do[a] aluno[a]: '))
    output = passfail(avaliacao)
    if avaliacao > 100:
        print('O número máximo de nota é 100')
    else:
        print(output)

except ValueError:
    print('Digite um número por favor.')
