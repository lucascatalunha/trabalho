def up_down(number: int) -> bool:
    if number > 0:
        return "Para cima"

    elif number < 0:
        return "Para baixo"

    elif number == 0:
        return "Zero"


if __name__ == "__main__":
    print(up_down(0))
