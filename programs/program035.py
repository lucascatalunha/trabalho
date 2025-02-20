def repeat_last_character_of_string_n_times(str1: str, times: int) -> str:
    return str1 + str1[len(str1) - 1] * (times - 1)


if __name__ == "__main__":
    print(
        repeat_last_character_of_string_n_times("hello", 3),
    )
