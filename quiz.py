import os
from time import sleep

os.system("cls")

pontuacao = 0

pergunta = str(input("Qual a capital do Brasil? "))

if pergunta.upper() == "BRASÍLIA":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital do Japão? "))

if pergunta.upper() == "TÓQUIO":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital dos Estados Unidos? "))

if pergunta.upper() == "WASHINGTON":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital da Holanda? "))

if pergunta.upper() == "AMSTERDÃ":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital da Austrália? "))

if pergunta.upper() == "CAMBERRA":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital da Inglaterra? "))

if pergunta.upper() == "LONDRES":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

pergunta = str(input("Qual a capital do Canadá? "))

if pergunta.upper() == "OTTAWA":
    print("Correta a resposta")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("Resposta incorreta")
    sleep(1)
    os.system("cls")

print("Processando pontuação...")
sleep(5)
os.system("cls")
porcentagem = (pontuacao / 7) * 100
porcentagem = float("{:.2f}".format(porcentagem))

print(f"Você acertou {porcentagem}% das perguntas ({pontuacao} de 7 perguntas)\nPontuação: {pontuacao} pontos\n")