def get_union_of_two_sets(conjunto1, conjunto2):
    return conjunto1 | conjunto2


if __name__ == "__main__":
    conjunto1 = {1, 2, 3}
    conjunto2 = {2, 3, 4}

    resultado = get_union_of_two_sets(conjunto1, conjunto2)
    print(resultado)
