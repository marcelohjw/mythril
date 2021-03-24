import random


class cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Pessoa:
    def __init__(self, tipo, nome, hp, mp, atka, atkb):
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.tipo = tipo
        self.nome = nome
        self.atka = atka
        self.atkb = atkb
        self.opcoes = ["Correr", "Atacar"]

    def definir_acao(self):
        i = 1
        print("\n" + cores.BOLD + self.nome + cores.ENDC)
        print(cores.OKBLUE + cores.BOLD + "Acoes" + cores.ENDC)
        for item in self.opcoes:
            print("    " + str(i) + ":", item)
            i += 1

    def status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.mp) + "/" + str(self.maxmp)

        print("                      HP                          MP")
        print("                      -------------------------------------------")
        print(cores.BOLD + self.nome + "(" + self.tipo + ")" + "   " + cores.OKGREEN +
              hp_string + "|" + hp_bar + "|  " +
              cores.OKBLUE + mp_string + "|" + mp_bar + "|" + cores.ENDC)

    def status_inimigo(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.mp) + "/" + str(self.maxmp)

        print("                      HP                          MP")
        print("                      -------------------------------------------")
        print(cores.BOLD + self.nome + "   " + cores.FAIL +
              hp_string + "|" + hp_bar + "|  " +
              cores.OKBLUE + mp_string + "|" + mp_bar + "|" + cores.ENDC)

    def gerar_dano(self):
        return random.randrange(self.atkb, self.atka)

    def levar_dano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def obter_hp(self):
        return self.hp


class Animal:
    def __init__(self, nome, hp, e, atka, atkb):
        self.hp = hp
        self.maxhp = hp
        self.maxenergia = e
        self.nome = nome
        self.energia = e
        self.atka = atka
        self.atkb = atkb

    def status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.energia / self.maxenergia) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.energia) + "/" + str(self.maxenergia)

        print("                      HP                          ENERGIA")
        print("                      -------------------------------------------")
        print(cores.BOLD + self.nome + "   " + cores.WARNING +
              hp_string + "|" + hp_bar + "|  " +
              cores.WARNING + mp_string + "|" + mp_bar + "|" + cores.ENDC)

    def status_animal(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        e_bar = ""
        e_ticks = (self.energia / self.maxenergia) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while e_ticks > 0:
            e_bar += "█"
            e_ticks -= 1

        while len(e_bar) < 10:
            e_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.energia) + "/" + str(self.maxenergia)

        print("                      HP                          ENERGIA")
        print("                      -------------------------------------------")
        print(cores.BOLD + self.nome + "   " + cores.WARNING +
              hp_string + "|" + hp_bar + "|  " +
              cores.WARNING + mp_string + "|" + e_bar + "|" + cores.ENDC)

    def gerar_dano(self):
        return random.randrange(self.atkb, self.atka)


    def levar_dano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def obter_hp(self):
        return self.hp