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
    def __init__(self, tipo, nome, hp, mp, atka, atkb, magias, equipamentos):
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.tipo = tipo
        self.nome = nome
        self.atka = atka
        self.atkb = atkb
        self.opcoes = ["Correr", "Atacar", "Verificar Equipamentos"]
        self.opcoes_bloq_1 = ["Correr", "Verificar Equipamentos"]
        self.opcoes_bloq_2 = ["Correr", "Atacar"]
        self.opcoes_mago = ["Correr", "Atacar", "Magia"]
        self.opcoes_mago_bloq_1 = ["Correr", "Atacar"]
        self.opcoes_mago_bloq_2 = ["Correr", "Magia"]
        self.opcoes_campones = ["Correr", "Atacar", "Cavar Buraco"]
        self.magias = magias
        self.equipamentos = equipamentos

    def definir_acao(self, bloq):
        i = 1
        print("\n" + cores.BOLD + self.nome + cores.ENDC)
        if self.tipo == "Guerreiro":
            # VALIDAR VARIAÇÃO DE AÇÕES
            if bloq:
                if(bloq == 1):
                    print(cores.FAIL + cores.BOLD + "Ações" + cores.ENDC)
                    for item in self.opcoes_bloq_1:
                        print("    " + str(i) + ":", item)
                        i += 1
                if(bloq == 2):
                    print(cores.FAIL + cores.BOLD + "Ações" + cores.ENDC)
                    for item in self.opcoes_bloq_2:
                        print("    " + str(i) + ":", item)
                        i += 1
            else:
                print(cores.FAIL + cores.BOLD + "Ações" + cores.ENDC)
                for item in self.opcoes:
                    print("    " + str(i) + ":", item)
                    i += 1
        elif self.tipo == "Mago":
            # VALIDAR VARIAÇÃO DE AÇÕES MAGO
            if bloq:
                if (bloq == 1):
                    print(cores.OKBLUE + cores.BOLD + "Ações" + cores.ENDC)
                    for item in self.opcoes_mago_bloq_1:
                        print("    " + str(i) + ":", item)
                        i += 1
                if (bloq == 2):
                    print(cores.OKBLUE + cores.BOLD + "Ações" + cores.ENDC)
                    for item in self.opcoes_mago_bloq_2:
                        print("    " + str(i) + ":", item)
                        i += 1
            else:
                print(cores.OKBLUE + cores.BOLD + "Ações" + cores.ENDC)
                for item in self.opcoes_mago:
                    print("    " + str(i) + ":", item)
                    i += 1
        elif self.tipo == "Campones":
            # VALIDAR VARIAÇÃO DE AÇÕES CAMPONES
            print(cores.WARNING + cores.BOLD + "Ações" + cores.ENDC)
            for item in self.opcoes_campones:
                print("    " + str(i) + ":", item)
                i += 1

    def definir_magia(self):
        i = 1
        print(cores.OKBLUE + cores.BOLD + "Magias" + cores.ENDC)
        for spell in self.magias:
            print("    " + str(i) + ":", spell.nome, "(Cost:", str(spell.custo) + ")")
            i += 1

    def escolha_equipamentos(self):
        i = 1
        print(cores.FAIL + cores.BOLD + "Equipamentos" + cores.ENDC)
        for equip in self.equipamentos:
            print("    " + str(i) + ":", equip.nome, "(Cost:", str(equip.custo) + ")")
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

        if self.tipo == "Guerreiro":
            print("                      HP                          ENERGIA")
            print("                      -------------------------------------------")
            print(cores.BOLD + self.nome + "(" + self.tipo + ")" + "   " + cores.OKGREEN +
                hp_string + "|" + hp_bar + "|  " +
                cores.WARNING + mp_string + "|" + mp_bar + "|" + cores.ENDC)
        elif self.tipo == "Mago":
            print("                      HP                          MP")
            print("                      -------------------------------------------")
            print(cores.BOLD + self.nome + "(" + self.tipo + ")" + "   " + cores.OKGREEN +
                hp_string + "|" + hp_bar + "|  " +
                cores.OKBLUE + mp_string + "|" + mp_bar + "|" + cores.ENDC)
        elif self.tipo == "Campones":
            print("                      HP                          ENERGIA")
            print("                      -------------------------------------------")
            print(cores.BOLD + self.nome + "(" + self.tipo + ")" + "   " + cores.OKGREEN +
                hp_string + "|" + hp_bar + "|  " +
                cores.WARNING + mp_string + "|" + mp_bar + "|" + cores.ENDC)

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

    def obter_mp(self):
        return self.mp

    def gastar_magia(self, tipo):
        if (tipo == 1):
            self.mp -= 20
            if self.mp <0:
                self.mp = 0
        if (tipo == 2):
            self.mp -= 20
            if self.mp <0:
                self.mp = 0
        if tipo == 3:
            self.mp -= 80
            if self.mp <0:
                self.mp = 0

    def gastar_energia(self, tipo):
        if (tipo == 1):
            self.mp -= 2
            if self.mp <0:
                self.mp = 0
        elif (tipo == 2):
            self.mp -= 3
            if self.mp <0:
                self.mp = 0
        elif (tipo == 3):
            self.mp -= 14
            if self.mp <0:
                self.mp = 0


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

    def gastar_energia(self):
        self.energia -= 10