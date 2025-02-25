def true_equations(equacao: str) -> bool:
    if "/" in equacao:
        str_1 = equacao.split("/")
        str_2 = str_1[1].split("=")
        str_3 = int(str_1[0]) / int(str_2[0])
        str_4 = str_2[1]
        if int(str_4) == str_3:
            print(equacao)
            return True
    else:
        print(equacao)
        return False

    if "*" in equacao:
        str_1 = equacao.split("*")
        str_2 = str_1[1].split("=")
        str_3 = int(str_1[0]) * int(str_2[0])
        str_4 = str_2[1]
        if int(str_4) == str_3:
            print(equacao)
            return True
    else:
        print(equacao)
        return False

    if "+" in equacao:
        str_1 = equacao.split("+")
        str_2 = str_1[1].split("=")
        str_3 = int(str_1[0]) + int(str_2[0])
        str_4 = str_2[1]
        if int(str_4) == str_3:
            print(equacao)
            return True
    else:
        print(equacao)
        return False

    if "-" in equacao:
        str_1 = equacao.split("-")
        str_2 = str_1[1].split("=")
        str_3 = int(str_1[0]) - int(str_2[0])
        str_4 = str_2[1]
        if int(str_4) == str_3:
            print(equacao)
            return True
    else:
        print(equacao)
        return False


if __name__ == "__main__":
    equacao = "5/5=1"
    print(true_equations(equacao))
