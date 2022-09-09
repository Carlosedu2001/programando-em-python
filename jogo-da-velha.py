import os

os.system("cls")

num = -1
contador = 1
vez = 0
a = '\033[0;30;40m1\033[m'
b = '\033[0;30;40m2\033[m'
c = '\033[0;30;40m3\033[m'
d = '\033[0;30;40m4\033[m'
e = '\033[0;30;40m5\033[m'
f = '\033[0;30;40m6\033[m'
g = '\033[0;30;40m7\033[m'
h = '\033[0;30;40m8\033[m'
i = '\033[0;30;40m9\033[m'

def verVencerdor(str):
        if a == 'X' and e == 'X' and i == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif c == 'X' and e == 'X' and g == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif a == 'X' and b == 'X' and c == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif a == 'X' and d == 'X' and g == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif g == 'X' and h == 'X' and i == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif c == 'X' and f == 'X' and i == 'X':
            print("\n\t\033[4;34;40mX VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif a == 'O' and e == 'O' and i == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif c == 'O' and e == 'O' and g == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif a == 'O' and b == 'O' and c == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif a == 'O' and d == 'O' and g == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif g == 'O' and h == 'O' and i == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()
        elif c == 'O' and f == 'O' and i == 'O':
            print("\n\t\033[4;33;40mO VENCEU\033[m")
            print("\n\n------ FIM DE JOGO ------\n\n")
            exit()

while contador < 10 and num != 0:
    jogoDaVelha = print(f"\n_{a}_|_{b}_|_{c}_\n_{d}_|_{e}_|_{f}_\n {g} | {h} | {i} ")

    verVencerdor(jogoDaVelha)
    
    num = int(input("\nDigite um número de 1 a 9: "))
    os.system("cls")
    if num == 1 and vez == 0 and a == '\033[0;30;40m1\033[m':
        a = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 2 and vez == 0 and b == '\033[0;30;40m2\033[m':
        b = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 3 and vez == 0 and c == '\033[0;30;40m3\033[m':
        c = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 4 and vez == 0 and d == '\033[0;30;40m4\033[m':
        d = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 5 and vez == 0 and e == '\033[0;30;40m5\033[m':
        e = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 6 and vez == 0 and f == '\033[0;30;40m6\033[m':
        f = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 7 and vez == 0 and g == '\033[0;30;40m7\033[m':
        g = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 8 and vez == 0 and h == '\033[0;30;40m8\033[m':
        h = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 9 and vez == 0 and i == '\033[0;30;40m9\033[m':
        i = 'X'
        contador = contador + 1
        vez = vez + 1
    elif num == 1 and vez == 1 and a == '\033[0;30;40m1\033[m':
        a = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 2 and vez == 1 and b == '\033[0;30;40m2\033[m':
        b = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 3 and vez == 1 and c == '\033[0;30;40m3\033[m':
        c = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 4 and vez == 1 and d == '\033[0;30;40m4\033[m':
        d = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 5 and vez == 1 and e == '\033[0;30;40m5\033[m':
        e = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 6 and vez == 1 and f == '\033[0;30;40m6\033[m':
        f = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 7 and vez == 1 and g == '\033[0;30;40m7\033[m':
        g = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 8 and vez == 1 and h == '\033[0;30;40m8\033[m':
        h = 'O'
        contador = contador + 1
        vez = vez - 1
    elif num == 9 and vez == 1 and i == '\033[0;30;40m9\033[m':
        i = 'O'
        contador = contador + 1
        vez = vez - 1

print("\n\t\033[4;31;40mEMPATE\033[m")
print("\n\n----- FIM DE JOGO -----\n\n")