from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal

import random

print("------------------------------------------------------------------------------------------")
print("Modos de Jogo:")

modos = ["1.    O jogo define a Classe por voce",
         "2.    Voce escolhe sua Classe"]

for modo in modos:
    print(modo)
quest = int(input("Voce deseja jogar em que modo? : "))
if quest == 2:
    from tree import rootwo
else:
    print("Sua classe sera escolhida de forma aleatoria!")
    nome = input("Qual o seu nome? : ")
    escolha = random.randrange(1, 4)
    if escolha == 1:
        print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
        # Instancia do Guerreiro
        player = Pessoa("Guerreiro", nome, 900, 10, 200, 70)
        player.status()
    if escolha == 2:
        print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
        # Instancia do Mago
        player = Pessoa("Mago", nome, 600, 150, 30, 15)
        player.status()
    if escolha == 3:
        print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Campones!")
        # Instancia do Campones
        player = Pessoa("Campones", nome, 200, 10, 10, 5)
        player.status()
    print("\n")

    # Instancia de Inimigos
    ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120)
    rato = Animal("Rato", 300, 20, 380, 250)

    ligar = True

    while ligar:
        print("----------------------------------------------------------")

        # Verificar se acabou
        if ladrao.obter_hp() == 0:
            print(cores.OKGREEN + "Voce Venceu " + ladrao.nome + "!" + cores.ENDC)
            ligar = False
        elif rato.obter_hp() == 0:
            print(cores.OKGREEN + "Voce Venceu " + rato.nome + "!" + cores.ENDC)
            ligar = False
        if player.obter_hp() == 0:
            print(cores.FAIL + "Voce Perdeu!" + cores.ENDC)
            print("==========================================================================================")
            novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
            novamente = novamente.lower()
            if novamente == "s":
                escolha2 = random.randrange(1, 4)
                if escolha2 == 1:
                    print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
                    # Instancia do Guerreiro
                    player = Pessoa("Guerreiro", nome, 900, 10, 200, 70)
                    player.status()
                if escolha2 == 2:
                    print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                    # Instancia do Mago
                    player = Pessoa("Mago", nome, 600, 150, 30, 15)
                    player.status()
                if escolha2 == 3:
                    print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Campones!")
                    # Instancia do Campones
                    player = Pessoa("Campones", nome, 200, 10, 10, 5)
                    player.status()
                    # Instancia de Inimigos
                    ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120)
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

            inimigo = random.randrange(1, 3)
            if inimigo == 1:
                print(cores.FAIL + "Confronto:", ladrao.nome + cores.ENDC)
                player.definir_acao()
                ladrao.status_inimigo()
                primeira_escolha = int(input("Escolha: "))
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
                            print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Guerreiro!")
                            # Instancia do Guerreiro
                            player = Pessoa("Guerreiro", nome, 900, 10, 200, 70)
                            player.status()
                        if escolha2 == 2:
                            print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                            # Instancia do Mago
                            player = Pessoa("Mago", nome, 600, 150, 30, 15)
                            player.status()
                        if escolha2 == 3:
                            print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Campones!")
                            # Instancia do Campones
                            player = Pessoa("Campones", nome, 200, 10, 10, 5)
                            player.status()
                            # Instancia de Inimigos
                            ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120)
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
                elif primeira_escolha == 2:
                    dano = str(player.gerar_dano())
                    print(
                        "Voce ataca " + ladrao.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                    ladrao.levar_dano(int(dano))
                    if ladrao.obter_hp() == 0:
                        print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                    else:
                        ladrao.status_inimigo()
                elif primeira_escolha == 3:
                    if player.tipo == "Campones":
                        print("Você cava um buraco e se joga nele escapando de seu inimigo!")
                        print(cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                        break
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
                    print(
                        ladrao.nome + " ataca voce e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com uma reada!")
                    player.status()

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
                            print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Guerreiro!")
                            # Instancia do Guerreiro
                            player = Pessoa("Guerreiro", nome, 900, 10, 200, 70)
                            player.status()
                        if escolha2 == 2:
                            print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                            # Instancia do Mago
                            player = Pessoa("Mago", nome, 600, 150, 30, 15)
                            player.status()
                        if escolha2 == 3:
                            print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,",
                                  "voce esta com a classe Campones!")
                            # Instancia do Campones
                            player = Pessoa("Campones", nome, 200, 10, 10, 5)
                            player.status()
                            # Instancia de Inimigos
                            ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120)
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
                elif primeira_escolha == 2:
                    dano = str(player.gerar_dano())
                    rato.levar_dano(int(dano))
                    print(
                        "Voce ataca " + rato.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
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
                else:
                    print("Digite 1 ou 2!")
                    continue
