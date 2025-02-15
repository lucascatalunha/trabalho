def odd_even(number: int) -> bool:
    if (number % 2) == 0:
        return "Even"

    else:
        return "Odd"


if __name__ == "__main__":
    print(odd_even(2))
