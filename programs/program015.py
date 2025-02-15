def minutes_into_seconds(minutes: int) -> int:
    return minutes * 60


if __name__ == "__main__":
    try:
        inputminutes = input(
            "Escreva um número de minutos quer queres converter em segundos: "
        )
        print(minutes_into_seconds(inputminutes))
    except ValueError:
        print("Escreva um número por favor.")
