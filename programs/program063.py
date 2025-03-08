def sum_of_all_evens_in_matrix(matriz):
    return sum(n for linha in matriz for n in linha if n % 2 == 0)


if __name__ == "__main__":
    print(sum_of_all_evens_in_matrix([[1, 2], [3, 4], [5, 6, 8]]))
