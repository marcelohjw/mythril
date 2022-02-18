from classes.config import cores
from classes.config import Pessoa
from classes.config import Animal

import random
import os

print("==========================================================================================")
print("Bem vindo ao mundo de " + cores.UNDERLINE + cores.FAIL + "Mythril" + cores.ENDC)
print("==========================================================================================")
print("Cuidado com os " + cores.FAIL + "ladrões" + cores.ENDC + " e " + cores.WARNING + "ratos" + "!" + cores.ENDC)
print("Ganhe um " + cores.FAIL + "confronto" + cores.ENDC + " para vencer o jogo!")

if os.path.isfile("./save.txt") and os.stat("./save.txt").st_size != 0:
    save_antigo = open("./save.txt", "r+")
    first_quest = input("Você se chama {}? Sim(S)/Nao(N): ".format(save_antigo.read()))
    if first_quest == "s":
        print("Bem vindo novamente!")
        from tree import rootone
    else:
        from tree import rootone
else:
    print(cores.FAIL + "Nome antigo nao encontrado..." + cores.ENDC)
    from tree import rootone