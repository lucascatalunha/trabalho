def average_of_number(*args) -> int:
    soma = 0
    for num in args:
        soma += num
        print(soma)
    print()
    return int(soma / len(args))


if __name__ == "__main__":
    print(average_of_number(1, 2, 3))
