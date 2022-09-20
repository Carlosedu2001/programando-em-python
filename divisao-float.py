from msvcrt import getch
import os

os.system("cls")

num = -1
div = 0
res = 0

while num != 0:
    num = float(input("Digite o número que quer saber a divisão: "))
    if num == 0:
        os.system("cls")
        exit()

    div = float(input("Digite o número por qual ele será dividido: "))
    if div == 0:
        os.system("cls")
        exit()

    res = num / div

    print(f"\n{num} / {div} = {res:.2f}")

    print("\nPressione ENTER para continuar")
    getch()
    os.system("cls")