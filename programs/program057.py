def repetir_letras(s, n):
    return "".join(c * n for c in s)


if __name__ == "__main__":
    print(repetir_letras("abc", 3))
