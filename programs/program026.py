def convert_to_titlecase(sentence: str) -> str:
    list_in = sentence.split(" ")
    list_out = []
    for frase in list_in:
        b = frase[0].upper()
        c = b + frase[1:]
        list_out.append(c)
    return " ".join(list_out)


if __name__ == "__main__":
    a = "hello world"
    print(convert_to_titlecase(a))
