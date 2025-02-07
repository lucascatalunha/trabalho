def hours_into_minutes(hours: int) -> int:
    return hours*60


try:
    inputhours = input(
        'Escreva um numero de horas quer queres converter em minutos: ')
    print(hours_into_minutes(inputhours))
except ValueError:
    print('Escreva um número por favor.')
