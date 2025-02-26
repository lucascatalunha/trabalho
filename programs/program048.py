def one_even_one_odd(sentence: str) -> int:
    for a in sentence:
        if int(a) % 2 == 0:
            return True
    for a in sentence:
        if int(a) % 2 != 0:
            return True

    # a = sentence.split("")
    # print(a)
    # # b = int(a[0])
    # # c = int(a[1])
    # if b % 2 == 0 and c % 2 != 0:
    #     print(sentence)
    #     return True


if __name__ == "__main__":
    sentence = "23"
    print(one_even_one_odd("23"))
