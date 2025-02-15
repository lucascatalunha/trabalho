def smiley_faces(str: str) -> str:
    list_in = str.split(":)")
    list_out = []
    for word in list_in:
        list_out.append(word)
    return "😀".join(list_out)


if __name__ == "__main__":
    frase = "How :) are :) you"
    print(smiley_faces(frase))
    #
