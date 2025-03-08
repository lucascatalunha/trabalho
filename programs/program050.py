def merge_two_dictionaries(dic1, dic2):
    return {**dic1, **dic2}


if __name__ == "__main__":
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    resultado = merge_two_dictionaries(d1, d2)
    print(resultado)
