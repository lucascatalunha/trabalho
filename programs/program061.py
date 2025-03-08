def intervalo_relogio(a, b):
    return min(abs(a - b), 12 - abs(a - b))


if __name__ == "__main__":
    print(intervalo_relogio(3, 9))
    print(intervalo_relogio(10, 2))
