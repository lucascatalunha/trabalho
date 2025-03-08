import math


def passengers_driver(total_passageiros, capacidade_por_viagem):
    return math.ceil(total_passageiros / capacidade_por_viagem)


if __name__ == "__main__":
    resultado = passengers_driver(12, 3)
    print(resultado)
