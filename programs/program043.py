def longest_consecutive_zeroes(bin_str):
    sequencias_zeros = bin_str.split("1")

    return max(len(sequencia) for sequencia in sequencias_zeros)


if __name__ == "__main__":
    bin_str = "10100100010001"
    resultado = longest_consecutive_zeroes(bin_str)
    print(resultado)
