def tem_letras_consecutivas(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


if __name__ == "__main__":
    print(tem_letras_consecutivas("hello"))
