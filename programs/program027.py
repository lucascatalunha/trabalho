def adding_ends(*list_1) -> int:
    return list_1[0] + list_1[len(list_1) - 1]


if __name__ == "__main__":
    print(adding_ends(1, 2, 3, 4))
