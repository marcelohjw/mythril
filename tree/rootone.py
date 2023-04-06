from distutils import core
from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal
from classes.magias import Magias
from classes.equipamentos import Equipamentos

import random

nome = input("Qual o seu nome? : ")
print(cores.OKGREEN + "INIT" + cores.ENDC)
escolha = random.randrange(1, 3)
if escolha == 1:
    # Instancia do Guerreiro O JOGO ESCOLHE
    faca = Equipamentos("Faca", 2, 70, "corpo")
    couro = Equipamentos("Couro", 3, 70, "tecido")
    goiaba = Equipamentos("Goiaba", 14, 70, "fruta")
    equipamentos = [faca, couro, goiaba]
    player = Pessoa("Guerreiro", nome, 900, 50, 200, 70, [], equipamentos)
    print()
    print("Olá", cores.FAIL + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Guerreiro!")
    player.status()
if escolha == 2:
    # Instancia do Mago O JOGO ESCOLHE
    fogo = Magias("Fogo", 20, 100, "basica")
    agua = Magias("Água", 20, 100, "basica")
    negra = Magias("Negra", 80, 400, "negra")
    magias_mago = [fogo, agua, negra]
    player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago, [])
    print()
    print("Olá", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
    player.status()
if escolha == 3:
    # Instancia do Campones O JOGO ESCOLHE
    player = Pessoa("Camponês", nome, 200, 10, 10, 5, [], [])
    print()
    print("Olá", cores.WARNING + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Camponês!")
    player.status()
print("\n")

# Instancia de Inimigos
ladrao = Pessoa("Ladrão", "Shrek", 600, 10, 200, 120, [], [])
rato = Animal("Rato", 300, 20, 380, 250)

ligar = True


# COMEÇA O JOGO PELA PRIMEIRA VEZ
while ligar:

    # VERIFICAR SE ACABOU
    if ladrao.obter_hp() == 0:
        ark = random.randrange(1, 3)
        if(ark == 2):
            print(cores.OKGREEN + "Você Venceu " + ladrao.nome + "!" + cores.ENDC)
            print(cores.OKGREEN + ladrao.nome + " derrubou o famoso Ark!!!" + cores.ENDC)
            ligar = False
        
    elif rato.obter_hp() == 0:
        ark = random.randrange(1, 3)
        if(ark == 2):
            print(cores.OKGREEN + "Você Venceu " + rato.nome + "!" + cores.ENDC)
            print(cores.OKGREEN + ladrao.nome + " derrubou o famoso Ark!!!" + cores.ENDC)
            ligar = False
    if player.obter_hp() == 0:
        print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
        print("==========================================================================================")
        novamente = input(cores.FAIL + "Tentar Novamente? Sim(S)/Nao(N): " + cores.ENDC)
        novamente = novamente.lower()
        if novamente == "s":
            escolha2 = random.randrange(1, 4)
            if escolha2 == 1:
                # Instancia do Guerreiro O JOGO ESCOLHE
                faca = Equipamentos("Faca", 2, 70, "corpo")
                couro = Equipamentos("Couro", 3, 70, "tecido")
                goiaba = Equipamentos("Goiaba", 14, 70, "fruta")
                equipamentos = [faca, couro, goiaba]
                player = Pessoa("Guerreiro", nome, 900, 50, 200, 70, [], equipamentos)
                print("Olá", cores.FAIL + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Guerreiro!")
                player.status()
            if escolha2 == 2:
                # Instancia do Mago O JOGO ESCOLHE
                fogo = Magias("Fogo", 20, 100, "basica")
                agua = Magias("Água", 20, 100, "basica")
                negra = Magias("Negra", 80, 400, "negra")
                magias_mago = [fogo, agua, negra]
                player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago, [])
                print("Olá", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
                player.status()
            if escolha2 == 3:
                # Instancia do Campones O JOGO ESCOLHE
                player = Pessoa("Campones", nome, 200, 10, 10, 5, [], [])
                print("Olá", cores.WARNING + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Campones!")
                player.status()
            # Instancia de Inimigos
            ladrao = Pessoa("Ladrão", "Shrek", 600, 10, 200, 120, [], [])
            rato = Animal("Rato", 300, 20, 380, 250)
            continue
        else:
            ligar = False
            questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
            questao = questao.lower()
            if questao == "s":
                print("Nome salvo:", nome)
                save_antigo = open("./save.txt", "w+")
                save_antigo.write(nome)
            break
    else:
        # JOGO CONTINUA
        print(cores.HEADER + "----------------------------------------------------------" + cores.ENDC)
        print(cores.HEADER + "NOVO TURNO" + cores.ENDC)
        print(cores.HEADER + "----------------------------------------------------------" + cores.ENDC)
        inimigo = random.randrange(1, 3)
        print()

        # INIMIGO LADRAO
        if inimigo == 1:
            print(cores.FAIL + "Confronto:", ladrao.nome + cores.ENDC)
            # EXIBIR VARIAÇÃO DE AÇÕES ALEATÓRIAS
            bloq = random.randrange(1, 2)
            print(bloq)
            player.definir_acao(bloq)
            ladrao.status_inimigo()

            while True:
                try:
                    primeira_escolha = int(input("Escolha: "))
                    break
                except:
                    print("Digite 1, 2 ou 3!")
            # ESCOLHA 1
            if primeira_escolha == 1:
                if player.tipo == "Campones":
                    print("Você consegue correr devido a sua grande agilidade de arador de campos")
                    print(cores.WARNING + "Você Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
                elif player.tipo == "Mago":
                    print("Você consegue correr mas deixa cair seu cajado")
                    print(
                        cores.OKBLUE + "Você Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
                print("Você consegue correr no momento em que vê ele mas deixa cair seu celular")
                print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                print("==========================================================================================")
                novamente = input(cores.FAIL + "Tentar Novamente? Sim(S)/Nao(N): " + cores.ENDC)
                novamente = novamente.lower()
                if novamente == "s":
                    escolha2 = random.randrange(1, 4)
                    if escolha2 == 1:
                        # Instancia do Guerreiro O JOGO ESCOLHE
                        faca = Equipamentos("Faca", 2, 70, "corpo")
                        couro = Equipamentos("Couro", 3, 70, "tecido")
                        goiaba = Equipamentos("Goiaba", 14, 70, "fruta")
                        equipamentos = [faca, couro, goiaba]
                        player = Pessoa("Guerreiro", nome, 900, 50, 200, 70, [], equipamentos)
                        print("Olá", cores.FAIL + player.nome + cores.ENDC, "bem vindo,",
                                "você está com a classe Guerreiro!")
                        player.status()
                    if escolha2 == 2:
                        # Instancia do Mago O JOGO ESCOLHE
                        fogo = Magias("Fogo", 20, 100, "basica")
                        agua = Magias("Água", 20, 100, "basica")
                        negra = Magias("Negra", 80, 400, "negra")
                        magias_mago = [fogo, agua, negra]
                        player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago, [])
                        print("Olá", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
                        player.status()
                    if escolha2 == 3:
                        # Instancia do Campones O JOGO ESCOLHE
                        player = Pessoa("Campones", nome, 200, 10, 10, 5, [], [])
                        print("Olá", cores.WARNING + player.nome + cores.ENDC, "bem vindo,",
                                "vocé está com a classe Campones!")
                        player.status()
                    # Instancia de Inimigos
                    ladrao = Pessoa("Ladrao", "Shrek", 600, 10, 200, 120, [], [])
                    rato = Animal("Rato", 300, 20, 380, 250)
                    continue
                else:
                    ligar = False
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
            # ESCOLHA 2
            elif primeira_escolha == 2:
                # BLOQ1
                if (bloq == 1):
                    # EXIBIR OPÇÕES 1
                    if player.tipo == "Mago":
                        dano = str(player.gerar_dano())
                        ladrao.levar_dano(int(dano))
                        print(
                            "Voce ataca " + ladrao.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.OKGREEN + "Voce Venceu " + ladrao.nome + "!" + cores.ENDC)
                            ligar = False
                    elif player.tipo == "Guerreiro":
                        print(cores.FAIL + "GUERREIRO ESCOLHENDO" + cores.ENDC)
                        player.escolha_equipamentos()
                        escolher_equipamento = input("Escolha: ")

                        # VERIFICAR ENERGIA
                        if player.obter_mp() == 0:
                            print("Seus pontos de energia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Equipamentos.gerar_dano_equipamento(int(escolher_equipamento)))
                        player.gastar_energia(int(escolher_equipamento))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Você ataca " + ladrao.nome + " com seu forte equipamento e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                # BLOQ2
                elif (bloq == 2):
                    # EXIBIR OPÇÕES 1
                    if player.tipo == "Mago":
                        print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")

                        # VERIFICAR MP
                        if player.obter_mp() == 0:
                            print("Seus pontos de magia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                        player.gastar_magia(int(escolher_magia))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Você ataca " + ladrao.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                    elif player.tipo == "Guerreiro":
                        print(cores.FAIL + "GUERREIRO ESCOLHENDO" + cores.ENDC)
                        player.escolha_equipamentos()
                        escolher_equipamento = input("Escolha: ")

                        # VERIFICAR ENERGIA
                        if player.obter_mp() == 0:
                            print("Seus pontos de energia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Equipamentos.gerar_dano_equipamento(int(escolher_equipamento)))
                        player.gastar_energia(int(escolher_equipamento))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Você ataca " + ladrao.nome + " com seu forte equipamento e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                dano = str(player.gerar_dano())
                print(
                    "Você ataca " + ladrao.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                ladrao.levar_dano(int(dano))
                if ladrao.obter_hp() == 0:
                    print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                else:
                    ladrao.status_inimigo()
            # ESCOLHA 3
            elif primeira_escolha == 3:
                if player.tipo == "Campones":
                    print("Você cava um buraco e se joga nele escapando de seu inimigo!")
                    print(cores.WARNING + "Você Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    break
                elif player.tipo == "Mago":
                    print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                    player.definir_magia()
                    escolher_magia = input("Escolha: ")

                    # VERIFICAR MP
                    if player.obter_mp() == 0:
                        print("Seus pontos de magia acabaram :(")
                        print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                        break

                    dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                    player.gastar_magia(int(escolher_magia))
                    ladrao.levar_dano(int(dano))
                    print(
                    "Você ataca " + ladrao.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                    if ladrao.obter_hp() == 0:
                        print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                    else:
                        ladrao.status_inimigo()
                elif player.tipo == "Guerreiro":
                    print(cores.FAIL + "GUERREIRO ESCOLHENDO" + cores.ENDC)
                    player.escolha_equipamentos()
                    escolher_equipamento = input("Escolha: ")

                    # VERIFICAR ENERGIA
                    if player.obter_mp() == 0:
                        print("Seus pontos de energia acabaram :(")
                        print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                        break

                    dano = str(Equipamentos.gerar_dano_equipamento(int(escolher_equipamento)))
                    player.gastar_energia(int(escolher_equipamento))
                    ladrao.levar_dano(int(dano))
                    print(
                    "Você ataca " + ladrao.nome + " com seu forte equipamento e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                    if ladrao.obter_hp() == 0:
                        print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                    else:
                        ladrao.status_inimigo()
            else:
                print("Digite 1, 2 ou 3!")
                print()
                print()
                continue
            if ladrao.obter_hp() == 0:
                inimigo == 2
                ark = random.randrange(1, 3)
                if(ark == 2):
                    print(cores.OKGREEN + "Você Venceu " + ladrao.nome + "!" + cores.ENDC)
                    print(cores.OKGREEN + ladrao.nome + " derrubou o famoso Ark!!!" + cores.ENDC)
                    ligar = False
            else:
                # Ataques do Inimigo Ladrao
                dano = str(ladrao.gerar_dano())
                ladrao.gastar_magia(4)
                player.levar_dano(int(dano))
                print()
                print(
                    ladrao.nome + " ataca você e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com uma reada!")
                player.status()

        # Inimigo RATO

        elif inimigo == 2:
            if ladrao.obter_hp() == 0:
                inimigo == 2
            print(cores.WARNING + "Confronto: " + rato.nome + cores.ENDC)
            rato.status_animal()
             # EXIBIR VARIAÇÃO DE AÇÕES ALEATÓRIAS
            bloq = random.randrange(1, 3)
            print(bloq)
            player.definir_acao(bloq)
            while True:
                try:
                    primeira_escolha = int(input("Escolha: "))
                    break
                except:
                    print("Digite 1, 2 ou 3!")
            if primeira_escolha == 1:
                if player.tipo == "Campones":
                    print("Você consegue correr devido a sua grande agilidade de arador de campos")
                    print(
                        cores.WARNING + "Você Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
                elif player.tipo == "Mago":
                    print("Você consegue correr mas deixa cair seu cajado :(")
                    print(
                        cores.OKBLUE + "Você Escapou! Os monstros ficaram vivos aterrorizando mythril!" + cores.ENDC)
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
                print("Você consegue correr no momento em que ve ele mas deixa cair seu celular")
                print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                print("==========================================================================================")
                novamente = input(cores.FAIL + "Tentar Novamente? Sim(S)/Nao(N): " + cores.ENDC)
                novamente = novamente.lower()
                if novamente == "s":
                    escolha2 = random.randrange(1, 4)
                    if escolha2 == 1:
                        # Instancia do Guerreiro O JOGO ESCOLHE
                        faca = Equipamentos("Faca", 2, 70, "corpo")
                        couro = Equipamentos("Couro", 3, 70, "tecido")
                        goiaba = Equipamentos("Goiaba", 14, 70, "fruta")
                        equipamentos = [faca, couro, goiaba]
                        player = Pessoa("Guerreiro", nome, 900, 50, 200, 70, [], equipamentos)
                        print("Olá", cores.FAIL + player.nome + cores.ENDC, "bem vindo,",
                                "você está com a classe Guerreiro!")
                        player.status()
                    if escolha2 == 2:
                        # Instancia do Mago O JOGO ESCOLHE
                        fogo = Magias("Fogo", 20, 100, "basica")
                        agua = Magias("Água", 20, 100, "basica")
                        negra = Magias("Negra", 80, 400, "negra")
                        magias_mago = [fogo, agua, negra]
                        player = Pessoa("Mago", nome, 600, 150, 30, 15, magias_mago, [])
                        print("Olá", cores.OKBLUE + player.nome + cores.ENDC, "bem vindo,", "você está com a classe Mago!")
                        player.status()
                    if escolha2 == 3:
                        # Instancia do Campones O JOGO ESCOLHE
                        player = Pessoa("Campones", nome, 200, 10, 10, 5, [], [])
                        print("Olá", cores.WARNING + player.nome + cores.ENDC, "bem vindo,",
                                "você está com a classe Campones!")
                        player.status()
                    # Instancia de Inimigos
                    ladrao = Pessoa("Ladrao", "Robertson", 600, 10, 200, 120, [], [])
                    rato = Animal("Jacaré", 300, 20, 380, 250)
                    continue
                else:
                    ligar = False
                    questao = input("Deseja salvar seu nome? Sim(S)/Nao(N): ")
                    questao = questao.lower()
                    if questao == "s":
                        print("Nome salvo:", nome)
                        save_antigo = open("./save.txt", "w+")
                        save_antigo.write(nome)
                    break
            elif primeira_escolha == 2:
                # BLOQ1
                if (bloq == 1):
                    # EXIBIR OPÇÕES 1
                    if player.tipo == "Mago":
                        print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")

                        # VERIFICAR MP
                        if player.obter_mp() == 0:
                            print("Seus pontos de magia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                        player.gastar_magia(int(escolher_magia))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Você ataca " + ladrao.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                    elif player.tipo == "Guerreiro":
                        print(cores.FAIL + "GUERREIRO ESCOLHENDO" + cores.ENDC)
                        player.escolha_equipamentos()
                        escolher_equipamento = input("Escolha: ")

                        # VERIFICAR ENERGIA
                        if player.obter_mp() == 0:
                            print("Seus pontos de energia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Equipamentos.gerar_dano_equipamento(int(escolher_equipamento)))
                        player.gastar_energia(int(escolher_equipamento))
                        ladrao.levar_dano(int(dano))
                        print(
                        "Você ataca " + ladrao.nome + " com seu forte equipamento e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if ladrao.obter_hp() == 0:
                            print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                        else:
                            ladrao.status_inimigo()
                # BLOQ2 - RATO
                elif (bloq == 2):
                    # EXIBIR DE ACORDO COM BLOQ 2
                    if player.tipo == "Mago":
                        print(cores.OKBLUE + "MAGO ESCOLHENDO" + cores.ENDC)
                        player.definir_magia()
                        escolher_magia = input("Escolha: ")

                        # VERIFICAR MP
                        if player.obter_mp() == 0:
                            print("Seus pontos de magia acabaram :(")
                            print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                            break

                        dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                        player.gastar_magia(int(escolher_magia))
                        rato.levar_dano(int(dano))
                        print(
                        "Você ataca " + rato.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                        if rato.obter_hp() == 0:
                            print(cores.FAIL + rato.nome + " foi derrotado." + cores.ENDC)
                        else:
                            rato.status_animal()
                    elif player.tipo == "Guerreiro":
                        dano = str(player.gerar_dano())
                        rato.levar_dano(int(dano))
                        print(
                            "Voce ataca " + rato.nome + " e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
                        if rato.obter_hp() == 0:
                            print(cores.OKGREEN + "Voce Venceu " + rato.nome + "!" + cores.ENDC)
                            ligar = False
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

                    # VERIFICAR MP
                    if player.obter_mp() == 0:
                        print("Seus pontos de magia acabaram :(")
                        print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                        break

                    player.gastar_magia(int(escolher_magia))
                    dano = str(Magias.gerar_dano_magico(int(escolher_magia)))
                    rato.levar_dano(int(dano))
                    print(
                    "Você ataca " + rato.nome + " com sua magia e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)!" + cores.ENDC)
                    if rato.obter_hp() == 0:
                        print(cores.FAIL + rato.nome + " foi derrotado." + cores.ENDC)
                    else:
                        rato.status_animal()
                elif player.tipo == "Guerreiro":
                    print(cores.FAIL + "GUERREIRO ESCOLHENDO" + cores.ENDC)
                    player.escolha_equipamentos()
                    escolher_equipamento = input("Escolha: ")

                    # VERIFICAR ENERGIA
                    if player.obter_mp() == 0:
                        print("Seus pontos de energia acabaram :(")
                        print(cores.FAIL + "Você Perdeu!" + cores.ENDC)
                        break

                    dano = str(Equipamentos.gerar_dano_equipamento(int(escolher_equipamento)))
                    player.gastar_energia(int(escolher_equipamento))
                    ladrao.levar_dano(int(dano))
                    print(
                    "Você ataca " + ladrao.nome + " com seu forte equipamento e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC)
                    if ladrao.obter_hp() == 0:
                        print(cores.FAIL + ladrao.nome + " foi derrotado." + cores.ENDC)
                    else:
                        ladrao.status_inimigo()
            else:
                print(cores.WARNING + "Digite 1, 2 ou 3!" + cores.ENDC)
                print()
                print()
            if rato.obter_hp() == 0:
                ark = random.randrange(1, 3)
                if(ark == 2):
                    print(cores.OKGREEN + "Você Venceu " + rato.nome + "!" + cores.ENDC)
                    print(cores.OKGREEN + ladrao.nome + " derrubou o famoso Ark!!!" + cores.ENDC)
                    ligar = False
            else:
                # Ataques do Inimigo Rato
                dano = str(rato.gerar_dano())
                rato.gastar_energia()
                player.levar_dano(int(dano))
                print(
                    rato.nome + " ataca você e atinge " + dano + " pontos de " + cores.FAIL + "vida(HP)" + cores.ENDC + " com sua leptospirose!")
                player.status()
                continue
