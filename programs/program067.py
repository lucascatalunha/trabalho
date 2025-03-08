def sum_of_two_smallest_numbers(lista):
    return sum(sorted(lista)[:2])


if __name__ == "__main__":
    print(sum_of_two_smallest_numbers([10, 15, 5, 8, 20]))
