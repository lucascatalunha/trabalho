def two_consecutive_identical_letters(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


if __name__ == "__main__":
    print(two_consecutive_identical_letters("hello"))
