def flash_cards(question: str, answer: str) -> str:
    dict_1 = {"question": question, "answer": answer}
    return dict_1


if __name__ == "__main__":
    print(flash_cards("Qual a capital da França?", "Paris"))
