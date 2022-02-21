from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal
from classes.magias import Magias


import random

print("Escolha com qual classe desejas jogar:")
i = 0

classes = ["Guerreiro", "Mago", "Campones"]
for claxx in classes:
    if claxx == "Mago":
        i += 1
        print(cores.OKBLUE + str(i), "-", claxx + cores.ENDC)
    elif claxx == "Guerreiro":
        i += 1
        print(cores.FAIL + str(i), "-", claxx + cores.ENDC)
    elif claxx == "Campones":
        i += 1
        print(cores.WARNING + str(i), "-", claxx + cores.ENDC)
escolha = int(input("Escolha: "))
nome = input("Qual o seu nome? ")
if escolha == 1:
    print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
    # Instancia do Guerreiro SUA ESCOLHA
    player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
    player.status()
if escolha == 2:
    print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
    # Instancia do Mago SUA ESCOLHA
    fogo = Magias("Fogo", 20, 100, "basica")
    agua = Magias("Água", 20, 100, "basica")
    negra = Magias("Negra", 80, 400, "negra")
    magias_mago = [fogo, agua, negra]
    player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago)
    player.status()
if escolha == 3:
    print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Campones!")
    # Instancia do Campones SUA ESCOLHA
    player = Pessoa("Campones", nome, 200, 10, 10, 5), []
    player.status()
print("\n")

# Instancia de Inimigos
ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120, [])
rato = Animal("Rato", 300, 20, 380, 250)

ligar = True

# COMEÇA O JOGO PELA PRIMEIRA VEZ
while ligar:
    print("----------------------------------------------------------")
    print(cores.HEADER + "NOVO TURNO" + cores.ENDC)
    print("----------------------------------------------------------")

    # Verificar se acabou
    if ladrao.obter_hp() == 0:
        print(cores.OKGREEN + "Voce Venceu " + ladrao.nome + "!" + cores.ENDC)
        ligar = False
    elif rato.obter_hp() == 0:
        print(cores.OKGREEN + "Voce Venceu " + rato.nome + "!" + cores.ENDC)
        ligar = False
    elif player.obter_hp() == 0:
        print(cores.FAIL + "Voce Perdeu!" + cores.ENDC)
        print("==========================================================================================")
        novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
        novamente = novamente.lower()
        questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
        questao = questao.lower()
        if questao == "s":
            print("Nome salvo:", nome)
            save_antigo = open("./save.txt", "w+")
            save_antigo.write(nome)

        if novamente == "s":
            escolha2 = random.randrange(1, 4)
            if escolha2 == 1:
                print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
                # Instancia do Guerreiro SUA ESCOLHA
                player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                player.status()
            if escolha2 == 2:
                print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                # Instancia do Mago SUA ESCOLHA
                player = Pessoa("Mago", nome, 600, 150, 30, 15, [])
                player.status()
            if escolha2 == 3:
                print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Campones!")
                # Instancia do Campones SUA ESCOLHA
                player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
                player.status()
                # Instancia de Inimigos
                ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120, [])
                rato = Animal("Rato", 300, 20, 380, 250)
            continue
        else:
            ligar = False
    else:

        inimigo = random.randrange(1, 3)
        # INIMIGO LADRÃO
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
                    break
                elif player.tipo == "Mago":
                    print("Voce consegue correr mas deixa cair seu cajado")
                    print(cores.OKBLUE + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    break
                print("Voce consegue correr no momento em que ve ele mas deixa cair seu celular")
                print(cores.FAIL + "Voce Perdeu!" + cores.ENDC)
                print("==========================================================================================")
                novamente = input("Tentar Novamente? Sim(S)/Nao(N): ")
                novamente = novamente.lower()

                questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                questao = questao.lower()
                if questao == "s":
                    print("Nome salvo:", nome)
                    save_antigo = open("./save.txt", "w+")
                    save_antigo.write(nome)

                if novamente == "s":
                    escolha2 = random.randrange(1, 4)
                    if escolha2 == 1:
                        print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
                        # Instancia do Guerreiro SUA ESCOLHA
                        player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                        player.status()
                    if escolha2 == 2:
                        print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                        # Instancia do Mago SUA ESCOLHA
                        player = Pessoa("Mago", nome, 600, 150, 30, 15, [])
                        player.status()
                    if escolha2 == 3:
                        print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,",
                              "voce esta com a classe Campones!")
                        # Instancia do Campones SUA ESCOLHA
                        player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
                        player.status()
                        # Instancia de Inimigos
                        ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120, [])
                        rato = Animal("Rato", 300, 20, 380, 250)
                    continue
                else:
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
                        print(cores.WARNING + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")
                        dano_magia_escolhida = Magias.gerar_dano_magico(escolher_magia)
                        print(
                            "Voce ataca " + ladrao.nome + " e atinge " + str(dano_magia_escolhida) + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        ladrao.levar_dano(int(dano_magia_escolhida))
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
                print(
                    ladrao.nome + " ataca voce e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com uma reada!")
                player.status()

        # INIMIGO RATO
        elif inimigo == 2:
            print(cores.WARNING + "Confronto: " + rato.nome + cores.ENDC)
            rato.status_animal()
            player.definir_acao()
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
                    print(cores.OKBLUE + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
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
                        print("Ola", cores.FAIL + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Guerreiro!")
                        # Instancia do Guerreiro SUA ESCOLHA
                        player = Pessoa("Guerreiro", nome, 900, 10, 200, 70, [])
                        player.status()
                    if escolha2 == 2:
                        print("Ola", cores.OKBLUE + nome + cores.ENDC, "bem vindo,", "voce esta com a classe Mago!")
                        # Instancia do Mago SUA ESCOLHA
                        player = Pessoa("Mago", nome, 600, 150, 30, 15, [])
                        player.status()
                    if escolha2 == 3:
                        print("Ola", cores.WARNING + nome + cores.ENDC, "bem vindo,",
                              "voce esta com a classe Campones!")
                        # Instancia do Campones SUA ESCOLHA
                        player = Pessoa("Campones", nome, 200, 10, 10, 5, [])
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
            # ESCOLHA 3
            elif primeira_escolha == 3:
                if player.tipo == "Campones":
                    print("Você cava um buraco e se joga nele escapando de seu inimigo!")
                    print(
                        cores.WARNING + "Voce Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    break
                elif player.tipo == "Mago":
                        print(cores.WARNING + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")
                        dano_magia_escolhida = Magias.gerar_dano_magico(escolher_magia)
                        print(
                            "Voce ataca " + rato.nome + " e atinge " + str(dano_magia_escolhida) + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        rato.levar_dano(int(dano_magia_escolhida))
                        if rato.obter_hp() == 0:
                            print(cores.FAIL + rato.nome + " foi derrotado." + cores.ENDC)
                        else:
                            rato.status()
                elif player.tipo == "Guerreiro":
                    print("MOSTRAR EQUIPAMENTOS")
            else:
                print("Digite 1, 2 ou 3!")