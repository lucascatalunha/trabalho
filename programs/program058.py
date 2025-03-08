def cubic_square(inicio, fim):
    return sum(int(d) for n in range(inicio, fim + 1) for d in str(n))


if __name__ == "__main__":
    print(cubic_square(10, 15))
