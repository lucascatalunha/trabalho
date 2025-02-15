def persons_information(name: str, city: str, age: int) -> dict:
    dict_info = {"name": name, "city": city, "age": age}
    return dict_info


if __name__ == "__main__":
    print(persons_information("Lucas", "Palmas", "15"))
