from distutils import core
from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal
from classes.magias import Magias

import random
import os

print("------------------------------------------------------------------------------------------")
print("Modos de Jogo:")

modos = ["1.    O jogo define a Classe por voce",
         "2.    Você escolhe sua Classe"]

for modo in modos:
    print(modo)
quest = int(input("Você deseja jogar em que modo? : "))
if quest == 2:
    from tree import rootwo
else:
    print("Sua classe será escolhida de forma aleatória!")
    if os.path.isfile("././save.txt") and os.stat("./save.txt").st_size != 0:
        save_antigo = open("./save.txt", "r+")
        nome = save_antigo.read()
    else:
        nome = input("Qual o seu nome? : ")
    #escolha = random.randrange(1, 4)
    escolha = 2
    if escolha == 1:
        # Instancia do Guerreiro O JOGO ESCOLHE
        player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
        print("Ola", cores.FAIL + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Guerreiro!")
        player.status()
    if escolha == 2:
        # Instancia do Mago O JOGO ESCOLHE
        fogo = Magias("Fogo", 20, 100, "basica")
        agua = Magias("Água", 20, 100, "basica")
        negra = Magias("Negra", 80, 400, "negra")
        magias_mago = [fogo, agua, negra]
        player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago)
        print("Ola", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
        player.status()
    if escolha == 3:
        # Instancia do Campones O JOGO ESCOLHE
        player = Pessoa("Camponês", nome, 200, 10, 10, 5, [])
        print("Ola", cores.WARNING + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Camponês!")
        player.status()
    print("\n")

    # Instancia de Inimigos
    ladrao = Pessoa("Ladrão", "Shrek", 600, 10, 200, 120, [])
    rato = Animal("Rato", 300, 20, 380, 250)

    ligar = True


    # COMEÇA O JOGO PELA PRIMEIRA VEZ
    while ligar:

        # VERIFICAR SE ACABOU
        if ladrao.obter_hp() == 0:
            print(cores.OKGREEN + "Você Venceu " + ladrao.nome + "!" + cores.ENDC)
            ligar = False
        elif rato.obter_hp() == 0:
            print(cores.OKGREEN + "Você Venceu " + rato.nome + "!" + cores.ENDC)
            ligar = False
        if player.obter_hp() == 0:
            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
            print("==========================================================================================")
            novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
            novamente = novamente.lower()
            if novamente == "s":
                escolha2 = random.randrange(1, 4)
                if escolha2 == 1:
                    # Instancia do Guerreiro O JOGO ESCOLHE
                    player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                    print("Olá", cores.FAIL + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Guerreiro!")
                    player.status()
                if escolha2 == 2:
                    # Instancia do Mago O JOGO ESCOLHE
                    fogo = Magias("Fogo", 20, 100, "basica")
                    agua = Magias("Água", 20, 100, "basica")
                    negra = Magias("Negra", 80, 400, "negra")
                    magias_mago = [fogo, agua, negra]
                    player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago)
                    print("Olá", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
                    player.status()
                if escolha2 == 3:
                    # Instancia do Campones O JOGO ESCOLHE
                    player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
                    print("Olá", cores.WARNING + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Campones!")
                    player.status()
                # Instancia de Inimigos
                ladrao = Pessoa("Ladrão", "Shrek", 600, 10, 200, 120, [])
                rato = Animal("Rato", 300, 20, 380, 250)
                continue
            else:
                questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                questao = questao.lower()
                if questao == "s":
                    print("Nome salvo:", nome)
                    save_antigo = open("./save.txt", "w+")
                    save_antigo.write(nome)
                break
        else:
            # JOGO CONTINUA
            print("----------------------------------------------------------")
            print(cores.HEADER + "NOVO TURNO" + cores.ENDC)
            print("----------------------------------------------------------")
            inimigo = random.randrange(1, 3)
            print()

            # INIMIGO LADRAO
            if inimigo == 1:
                print(cores.FAIL + "Confronto:", ladrao.nome + cores.ENDC)
                player.definir_acao()
                ladrao.status_inimigo()
                primeira_escolha = int(input("Escolha: "))
                # ESCOLHA 1
                if primeira_escolha == 1:
                    if player.tipo == "Campones":
                        print("Voce consegue correr devido a sua grande agilidade de arador de campos")
                        print(cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                    elif player.tipo == "Mago":
                        print("Voce consegue correr mas deixa cair seu cajado")
                        print(
                            cores.OKBLUE + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                    print("Voce consegue correr no momento em que ve ele mas deixa cair seu celular")
                    print(cores.FAIL + "Voce Perdeu!" + cores.ENDC)
                    print("==========================================================================================")
                    novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
                    novamente = novamente.lower()
                    if novamente == "s":
                        escolha2 = random.randrange(1, 4)
                        if escolha2 == 1:
                            # Instancia do Guerreiro O JOGO ESCOLHE
                            player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                            print("Ola", cores.FAIL + player.nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Guerreiro!")
                            player.status()
                        if escolha2 == 2:
                            # Instancia do Mago O JOGO ESCOLHE
                            fogo = Magias("Fogo", 20, 100, "basica")
                            agua = Magias("Água", 20, 100, "basica")
                            negra = Magias("Negra", 80, 400, "negra")
                            magias_mago = [fogo, agua, negra]
                            player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago)
                            print("Ola", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                            player.status()
                        if escolha2 == 3:
                            # Instancia do Campones O JOGO ESCOLHE
                            player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
                            print("Ola", cores.WARNING + player.nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Campones!")
                            player.status()
                        # Instancia de Inimigos
                        ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120, [])
                        rato = Animal("Rato", 300, 20, 380, 250)
                        continue
                    else:
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                # ESCOLHA 2
                elif primeira_escolha == 2:
                    dano = str(player.gerar_dano())
                    print(
                        "Voce ataca " + ladrao.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                    ladrao.levar_dano(int(dano))
                    if ladrao.obter_hp() == 0:
                        print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                    else:
                        ladrao.status_inimigo()
                # ESCOLHA 3
                elif primeira_escolha == 3:
                    if player.tipo == "Campones":
                        print("Você cava um buraco e se joga nele escapando de seu inimigo!")
                        print(cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        break
                    elif player.tipo == "Mago":
                        print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")
                        dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Voce ataca " + ladrao.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                    elif player.tipo == "Guerreiro":
                        print("MOSTRAR EQUIPAMENTOS")
                else:
                    print("Digite 1, 2 ou 3!")
                    continue
                if ladrao.obter_hp() == 0:
                    print(cores.OKGREEN + "Voce Venceu " + ladrao.nome + "!" + cores.ENDC)
                    ligar = False
                else:
                    # Ataques do Inimigo Ladrao
                    dano = str(ladrao.gerar_dano())
                    player.levar_dano(int(dano))
                    print()
                    print(
                        ladrao.nome + " ataca voce e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com uma reada!")
                    player.status()

            # Inimigo RATO

            elif inimigo == 2:
                print(cores.WARNING + "Confronto: " + rato.nome + cores.ENDC)
                rato.status_animal()
                player.definir_acao()
                primeira_escolha = int(input("Escolha: "))
                if primeira_escolha == 1:
                    if player.tipo == "Campones":
                        print("Voce consegue correr devido a sua grande agilidade de arador de campos")
                        print(
                            cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                    elif player.tipo == "Mago":
                        print("Voce consegue correr mas deixa cair seu cajado")
                        print(
                            cores.OKBLUE + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                    print("Voce consegue correr no momento em que ve ele mas deixa cair seu celular")
                    print(cores.FAIL + "Voce Perdeu!" + cores.ENDC)
                    print("==========================================================================================")
                    novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
                    novamente = novamente.lower()
                    if novamente == "s":
                        escolha2 = random.randrange(1, 4)
                        if escolha2 == 1:
                            # Instancia do Guerreiro O JOGO ESCOLHE
                            player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                            print("Ola", cores.FAIL + player.nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Guerreiro!")
                            player.status()
                        if escolha2 == 2:
                            # Instancia do Mago O JOGO ESCOLHE
                            fogo = Magias("Fogo", 20, 100, "basica")
                            agua = Magias("Água", 20, 100, "basica")
                            negra = Magias("Negra", 80, 400, "negra")
                            magias_mago = [fogo, agua, negra]
                            player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago)
                            print("Ola", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                            player.status()
                        if escolha2 == 3:
                            # Instancia do Campones O JOGO ESCOLHE
                            player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
                            print("Ola", cores.WARNING + player.nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Campones!")
                            player.status()
                        # Instancia de Inimigos
                        ladrao = Pessoa("Ladrao", "Robertson", 600, 10, 200, 120, [])
                        rato = Animal("Jacaré", 300, 20, 380, 250)
                        continue
                    else:
                        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                        questao = questao.lower()
                        if questao == "s":
                            print("Nome salvo:", nome)
                            save_antigo = open("./save.txt", "w+")
                            save_antigo.write(nome)
                        break
                elif primeira_escolha == 2:
                    dano = str(player.gerar_dano())
                    rato.levar_dano(int(dano))
                    print(
                        "Voce ataca " + rato.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
                    rato.status_animal()
                    print()
                elif primeira_escolha == 3:
                    if player.tipo == "Campones":
                        print("Você cava um buraco e se joga nele escapando de seu inimigo!")
                        print(cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        break
                    elif player.tipo == "Mago":
                        print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")
                        dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                        rato.levar_dano(int(dano))
                        print(
                        "Voce ataca " + rato.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
                        if rato.obter_hp() == 0:
                            print(cores.FAIL + rato.nome + " foi derrotado." + cores.ENDC)
                        else:
                            rato.status_animal()
                    elif player.tipo == "Guerreiro":
                        print(cores.FAIL + "EQUIPAMENTOS" + cores.ENDC)
                else:
                    print("Digite 1, 2 ou 3!")
                if rato.obter_hp() == 0:
                    print(cores.OKGREEN + "Voce Venceu " + rato.nome + "!" + cores.ENDC)
                    ligar = False
                else:
                    # Ataques do Inimigo Rato
                    dano = str(rato.gerar_dano())
                    player.levar_dano(int(dano))
                    print(
                        rato.nome + " ataca voce e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com sua leptospirose!")
                    player.status()
                    continue
