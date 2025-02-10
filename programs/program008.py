def is_number_odd(number: int) -> bool:
    if (number % 2) != 0:
        return True

    else:
        return False


if __name__ == "__main__":
    try:
        pessoa = int(input("Digite um número: "))

        output = is_number_odd(pessoa)
        print(pessoa)
        print(output)

    except ValueError:
        print("Digite um número por favor.")
