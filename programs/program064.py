def vowel_word_start(frase):
    return [palavra for palavra in frase.split() if palavra[0].lower() in "aeiou"]


if __name__ == "__main__":
    print(vowel_word_start("These are apple and orange"))
