def passfail(a: int) -> str:
    if a < 50:
        return "Failed"
    else:
        return "Passed"


if __name__ == "__main__":
    try:
        avaliacao = int(input("Digite a nota do[a] aluno[a]: "))
        output = passfail(avaliacao)

        print(output)

    except ValueError:
        print("Digite um número por favor.")
