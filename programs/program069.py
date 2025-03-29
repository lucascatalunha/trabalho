# 2. Calcular custo total
def shopping_for_memorial_day(custos):
    return sum(map(int, custos.split()))


if __name__ == "__main__":
    shopping_for_memorial_day(10)
