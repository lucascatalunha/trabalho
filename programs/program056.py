import math


def calcular_viagens(total_passageiros, capacidade_por_viagem):
    return math.ceil(total_passageiros / capacidade_por_viagem)


if __name__ == "__main__":
    resultado = calcular_viagens(12, 3)
    print(resultado)
