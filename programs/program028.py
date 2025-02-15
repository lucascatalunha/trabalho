def add_even(*number: int) -> bool:
    list_even_number = []
    for even_number in number:
        if (even_number % 2) == 0:
            list_even_number.append(even_number)
        else:
            continue
    b = 0
    for numbers in list_even_number:
        b += numbers
    return b


if __name__ == "__main__":
    print(add_even(1, 2, 3, 4, 5))
