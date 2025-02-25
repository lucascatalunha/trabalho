def shortest_word_in_string(sentence: str) -> bool:
    str_1 = sentence.split(" ")
    word_len_max = 255
    word_selected = ""
    for word in str_1:
        if len(word) < word_len_max:
            word_selected = word
            word_len_max = len(word)
    print(word_len_max)
    return word_selected


if __name__ == "__main__":
    sentence = "This is an example"
    print(shortest_word_in_string(sentence))
