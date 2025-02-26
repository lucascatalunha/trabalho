def tallest_birthday_cake_candles(*sentence) -> int:
    number_min = 0
    number_count = 0
    for number in sentence:
        if number == number_min:
            number_count += 1

        if number > number_min:
            number_min = number
            number_count = 1

    return number_count, number_min


if __name__ == "__main__":
    sentence = [1, 2, 3, 4, 4]
    print(tallest_birthday_cake_candles(1, 2, 3, 4, 4, 3, 3))
