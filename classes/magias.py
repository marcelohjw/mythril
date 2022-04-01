import random


class Magias:
    def __init__(self, nome, custo, dano, tipo):
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.tipo = tipo

    def gerar_dano_magico(tipo):
        if (tipo == 3):
            # Magia Negra
            baixo = 80
            alto = 300
        else:
            baixo = 50
            alto = 100
        return random.randrange(baixo, alto)
