def repeat_last_character_of_string_n_times(txt: str, word1: int, word2: int) -> str:
    return txt.replace(word1, word2)


if __name__ == "__main__":
    txt = "I like bananas"
    print(
        repeat_last_character_of_string_n_times(txt, "bananas", "apples"),
    )
