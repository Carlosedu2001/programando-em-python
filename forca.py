import os
import random
from time import sleep

os.system("cls")

dificuldade = 0
erros = 0
l_digitadas = []
palavra = ''
letra = ''

facil = ["Lousa", "Cachorro", "Gato", "Bola", "Barco", "Cama", "Casa"]
medio = ["Beija-Flor", "Guarda-Sol", "Guarda-Chuva", "Quebra-Cabeça", "Arco-Íris", "Cachorro-Quente"]
dificil = ["Tigre-Dentes-de-Sabre", "Otorrinolaringologista", "Interdisciplinaridade", "Hiperintelectualidade", "Compartimentalização"]
aleatorio = [facil + medio + dificil]

modo = str(input("Dificuldade\n\nDigite F para 'Fácil', M para 'Médio', D para 'Difícil' ou A para 'Aleatório': "))

if modo.upper() == 'F':
    dificuldade = facil
elif modo.upper() == 'M':
    dificuldade = medio
elif modo.upper() == 'D':
    dificuldade = dificil.upper()
elif modo.upper() == 'A':
    dificuldade = aleatorio.upper()
else:
    os.system("cls")
    print("Valor inválido")
    exit()

palavra = random.choice(dificuldade).upper()

def forca():

    if erros == 0:
        print('''
            _____
           |     |
                 |
                 |
                 |
                _|_''')
    if erros == 1:
        print('''
            _____
           |     |
           O     |
                 |
                 |
                _|_''')
    if erros == 2:
        print('''
            _____
           |     |
           O     |
           |     |
           |     |
                _|_''')
    if erros == 3:
        print('''
            _____
           |     |
           O     |
           |     |
           |     |
            \   _|_''')
    if erros == 4:
        print('''
            _____
           |     |
           O     |
           |     |
           |     |
          / \   _|_''')
    if erros == 5:
        print('''
            _____
           |     |
           O     |
           |\    |
           |     |
          / \   _|_''')
    if erros == 6:
        print('''
            _____
           |     |
           O     |
          /|\    |
           |     |
          / \   _|_''')

def substitui():

    l_faltando = palavra.__len__()
    acertos = 0

    for l in palavra:
        if l in l_digitadas:
            print(l, end=' ')
            acertos += 1
        else:
            print("_", end=' ')

    print(f"\tLetras digitadas: {l_digitadas}\tLetras faltando: {l_faltando - acertos}")

    if l_faltando - acertos == 0:
        os.system("cls")
        forca()
        print(f"\nPalavra: {palavra}")
        print("\nParabéns, você venceu")
        exit()
    else:
        pass

while erros < 6:
    os.system("cls")
    forca()

    print("\n")

    substitui()

    letra = str(input("\n\nDigite uma letra: ")).upper()

    if letra == 'SAIR':
        exit()

    if letra in palavra and letra not in l_digitadas and letra != '':
        print("Você acertou")
        l_digitadas.append(letra)
        sleep(1.5)
    elif letra not in palavra and letra not in l_digitadas:
        print("Você errou")
        l_digitadas.append(letra)
        erros += 1
        sleep(1.5)
    else:
        print("Valor inválido")
        sleep(1.5)

if erros == 6:
    os.system("cls")
    forca()
    print(f"\nA palavra era: {palavra}")
else:
    pass