def club_entry(input1: int) -> bool:
    if input1 >= 18:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        pessoa = int(input("Digite sua idade: "))

        output = club_entry(pessoa)
        print(output)

    except ValueError:
        print("Digite um número por favor.")
