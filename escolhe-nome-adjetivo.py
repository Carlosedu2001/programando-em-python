import os
from random import *
from time import sleep

os.system("cls")

embaralhadorM = []
embaralhadorF = []
mf = ''
adjetivosM = ["Bonito", "Vaidoso", "Educado", "Engraçado", "Gentil", "Brilhante", "Inteligente", "Visionário", "FANTÁSTICO"]
adjetivosF = ["Bonita", "Vaidosa", "Educada", "Engraçada", "Gentil", "Brilhante", "Inteligente", "Visionária", "FANTÁSTICA"]

while mf.upper() != "SAIR":
    print("Digite 'SAIR' para sair\n")
    mf = str(input("Digite 'M' para adcionar um nome masculino ou 'F' para adicionar um nome feminino: "))
    if mf.upper() == 'M':
        mf = str(input("Digite um nome: "))
        embaralhadorM.append(mf)
        os.system("cls")
    elif mf.upper() == 'F':
        mf = str(input("Digite um nome: "))
        embaralhadorF.append(mf)
        os.system("cls")

if embaralhadorM.__len__() == 0 or embaralhadorF.__len__() == 0:
    os.system("cls")
    print("Necessário pelo menos 1 nome em cada sexo\n")
    exit()

shuffle(adjetivosM)
shuffle(adjetivosF)
shuffle(embaralhadorM)
shuffle(embaralhadorF)

os.system("cls")
print("Preparando...")
sleep(5)
os.system("cls")

print(f"{embaralhadorM[0]} {adjetivosM[0]}")
print(f"{embaralhadorF[0]} {adjetivosF[0]}\n")