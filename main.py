from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal

import random
import os

# TAMANHO FIXO TERMINAL
os.system("mode con: cols=25 lines=95")

print("==========================================================================================")
print("Bem vindo ao mundo de " + cores.UNDERLINE + cores.FAIL + "Mythril" + cores.ENDC)
print("==========================================================================================")
print("Cuidado com os " + cores.FAIL + "ladrões" + cores.ENDC + " e " + cores.WARNING + "ratos" + "!" + cores.ENDC)
print("Obtenha o famoso " + cores.OKGREEN + "Ark" + cores.ENDC + " para vencer o jogo!")

if os.path.isfile("./save.txt") and os.stat("./save.txt").st_size != 0:
    save_antigo = open("./save.txt", "r+")
    first_quest = input("Você se chama {}? Sim(S)/Nao(N): ".format(save_antigo.read()))
    if first_quest == "s":
        print("Bem vindo novamente!")
        from story import storyline
    else:
       from story import storyline
else:
    print(cores.FAIL + "Nome antigo não encontrado..." + cores.ENDC)
    print("------------------------------------------------------------------------------------------")
    print("Modos de Jogo:")

    modos = ["1.    O jogo define a Classe por você",
            "2.    Você escolhe sua Classe"]

    for modo in modos:
        print(modo)

    # LOOP para validar o int no input
    while True:
        try:
            quest = int(input("Você deseja jogar em que modo? : "))
            break
        except:    
            print("Digite 1 ou 2!")

    if quest == 2:
        from tree import rootwo
    elif quest == 1:
        from tree import rootone