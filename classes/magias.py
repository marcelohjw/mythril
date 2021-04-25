import random


class Magias:
    def __init__(self, nome, custo, dano, tipo):
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.tipo = tipo

    def gerar_dano_magico(self):
        baixo = self.dmg - 15
        alto = self.dmg + 15
        return random.randrange(baixo, alto)
