import random


class Equipamentos:
    def __init__(self, nome, custo, dano, tipo):
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.tipo = tipo

    def gerar_dano_equipamento(tipo):
        if (tipo == "corpo"):
            baixo = 10
            alto = 70
        elif (tipo == "tecido"):
            baixo = 4
            alto = 33
        elif (tipo == "fruta"):
            baixo = 112
            alto = 444
        else:
            baixo = 50
            alto = 100
        return random.randrange(baixo, alto)
