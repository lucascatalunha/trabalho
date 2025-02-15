def is_number_even(number: int) -> bool:
    if (number % 2) == 0:
        return "Even"

    else:
        return "Odd"


if __name__ == "__main__":
    print(is_number_even(2))
