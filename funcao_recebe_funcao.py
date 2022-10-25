import os

os.system("cls")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultados(funcao, a, b):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultados(somar, 1, 2)
exibir_resultados(subtrair, 1, 2)
exibir_resultados(multiplicar, 1, 2)
exibir_resultados(dividir, 1, 2)

operacao = str(input("\nDigite qual operação deseja fazer -> (Soma), (Subtração), (Multiplicação) ou (Divisão): "))
valor1 = int(input("\nDigite o primeiro valor: "))
valor2 = int(input("\nDigite o segundo valor: "))

if operacao.title() == "Soma":
    os.system("cls")
    exibir_resultados(somar, valor1, valor2)
elif operacao.title() == "Subtração":
    os.system("cls")
    exibir_resultados(subtrair, valor1, valor2)
elif operacao.title() == "Multiplicação":
    os.system("cls")
    exibir_resultados(multiplicar, valor1, valor2)
elif operacao.title() == "Divisão":
    os.system("cls")
    exibir_resultados(dividir, valor1, valor2)
else:
    os.system("cls")
    print("Valores Inválidos")
    exit()