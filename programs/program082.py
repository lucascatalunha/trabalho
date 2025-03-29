# 14. Retornar dia da semana
def dia_da_semana(n):
    dias = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo",
    ]
    return dias[n - 1] if 1 <= n <= 7 else "Número inválido"
