from msvcrt import getch
import os

os.system("cls")

mult = -1

while mult != 0:
    print("Digite 0 para sair\n")
    mult = int(input("Qual tabuada você quer saber? "))
    if mult == 0:
        os.system("cls")
        exit()
    os.system("cls")
    for i in range (1, 11):
        res = mult * i
        print(f"{mult} x {i} = {res}")
        
    print("\nPressione ENTER para continuar")
    getch()
    os.system("cls")