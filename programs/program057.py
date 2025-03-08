def repeating_letters_n_times(s, n):
    return "".join(c * n for c in s)


if __name__ == "__main__":
    print(repeating_letters_n_times("abc", 3))
