def free_throw_probability(freethrow: int, attempts: int) -> float:
    return freethrow / attempts


if __name__ == "__main__":
    print(free_throw_probability(2, 5))
