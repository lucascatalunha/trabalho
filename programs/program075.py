def saudacao(pais):
    saudacoes = {
        "EUA": "Hello",
        "França": "Bonjour",
        "Espanha": "Hola",
        "Itália": "Ciao",
    }
    return saudacoes.get(pais, "Saudação não encontrada")
