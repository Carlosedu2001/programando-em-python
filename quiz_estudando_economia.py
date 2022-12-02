import os
from time import sleep

os.system("cls")

pontuacao = 0

pergunta = str(input("Quais os 4 objetivos da Política Macroeconômica? (Escrever no formato: C, E, D e P)\nR: "))

if pergunta.upper() == "CRESCIMENTO ECONÔMICO, ESTABILIDADE DE PREÇOS, DISTRIBUIÇÃO DE RENDA SOCIALMENTE JUSTA E PLENO EMPREGO DOS FATORES DE PRODUÇÃO":
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

pergunta = str(input("Inflação é o aumento contínuo e generalizado de preços, da maioria dos bens e serviços na economia. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Inflação de demanda ocorre com o aumento de custo de fatores de produção de bens e serviços. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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

pergunta = str(input("As estruturas de mercado monopólio e oligopólio, favorecem o aumento contínuo e generalizado de preços, da maioria dos bens e serviços na economia. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Desvalorização cambial é o aumento na taxa de câmbio. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("NGP é nível geral de preços da economia. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("A Contabilidade Nacional, trata de aspectos econômicos “Ex Post” e a Contabilidade Social de aspectos “Ex ante”. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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

pergunta = str(input("A moeda atualmente tem lastro em ouro , sua aceitação é através de “curso forçado”. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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

pergunta = str(input("Demanda Agregada, pode ser obtida através de: C + I + G + (X + M). (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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

pergunta = str(input("Sobre a fórmula de Demanda Agregada, C corresponde a: "))

if pergunta.upper() == "CONSUMO":
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

pergunta = str(input("Sobre a fórmula de Demanda Agregada, I corresponde a: "))

if pergunta.upper() == "INVESTIMENTO" or pergunta.upper() == "INVESTIMENTOS":
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

pergunta = str(input("Sobre a fórmula de Demanda Agregada, G corresponde a: "))

if pergunta.upper() == "GASTOS" or pergunta.upper() == "GASTOS DO GOVERNO" or pergunta.upper() == "GASTOS GOVERNAMENTAIS":
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

pergunta = str(input("Sobre a fórmula de Demanda Agregada, X corresponde a: "))

if pergunta.upper() == "EXPORTAÇÃO" or pergunta.upper() == "EXPORTAÇÕES":
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

pergunta = str(input("Sobre a fórmula de Demanda Agregada, M corresponde a: "))

if pergunta.upper() == "IMPORTAÇÃO" or pergunta.upper() == "IMPORTAÇÕES":
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

pergunta = str(input("Ainda sobre a fórmula de Demanda Agregada (DA), pode-se dizer que DA = RN = Y (VERDADEIRO OU FALSO)?\nVale lembrar que: RN = Renda Nacional e Y = PIB\nR: "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Ainda sobre a fórmula de Demanda Agregada: C + I + G + (X - M)? (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("De forma resumida qual é a função da SELIC na economia? "))

if pergunta.upper() == "BUSCAR O CONTROLE DA INFLAÇÃO" or pergunta.upper() == "BUSCAR O CONTROLE INFLACIONÁRIO" or pergunta.upper() == "CONTROLE INFLACIONÁRIO" or pergunta.upper() == "CONTROLAR A INFLAÇÃO":
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

pergunta = str(input("O que é a SELIC? "))

if pergunta.upper() == "É A TAXA REFERENCIAL DE JUROS DA ECONOMIA BRASILEIRA" or pergunta.upper() == "É A TAXA REFERENCIAL DOS JUROS DA ECONOMIA BRASILEIRA":
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

pergunta = str(input("Quem define a SELIC? "))

if pergunta.upper() == "COPOM":
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

pergunta = str(input("Considerando os dados: C = 95 + 0,8RN, I = 460, G = 130, T = 80, X = 250, M = 250\nDetermine a RN: "))

if pergunta.upper() == "3425":
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

pergunta = str(input("Sobre a estrutura da fórmula KEYNESIANA, é correto dizer: k = 1 / (1 - PMC)? "))

if pergunta.upper() == "SIM":
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

pergunta = str(input("Sobre a estrutura da fórmula KEYNESIANA, é correto dizer: k = 1 / PMP? "))

if pergunta.upper() == "SIM":
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

pergunta = str(input("O que significa PMC na fórmula: k = 1 / (1 - PMC)? "))

if pergunta.upper() == "PROPENSÃO MARGINAL A CONSUMIR":
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

pergunta = str(input("O que significa PMP na fórmula: k = 1 / PMP? "))

if pergunta.upper() == "PROPENSÃO MARGINAL A POUPAR":
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

pergunta = str(input("O que significa K na fórmula: k = 1 / (1 - PMC)? "))

if pergunta.upper() == "MULTIPLICADOR KEYNESIANO":
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

pergunta = str(input("Considerando os dados: C = 95 + 0,8RN, I = 460, G = 130, T = 80, X = 250, M = 250\nDetermine K: "))

if pergunta.upper() == "5":
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

pergunta = str(input("Sobre a Integração econômica internacional, qual o total de etapas? "))

if pergunta.upper() == "5":
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

pergunta = str(input("Ainda sobre Integração econômica internacional, quais são suas etapas?\nEscrever na estrutura: Z, U, M, U e U\nR: "))

if pergunta.upper() == "ZONA DE LIVRE COMÉRCIO, UNIÃO ADUANEIRA, MERCADO COMUM, UNIÃO ECONÔMICA E UNIÃO DE INTEGRAÇÃO TOTAL" or pergunta.upper() == "ZONA DE LIVRE COMÉRCIO, UNIÃO ADUANEIRA, MERCADO COMUM, UNIÃO MONETÁRIA E UNIÃO DE INTEGRAÇÃO TOTAL":
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

pergunta = str(input("Ainda sobre Integração econômica internacional, é correto afirmar que: Zona de livre comércio (ZLC)\nUnião aduaneira (UA)\nMercado comum (MC)\nUnião econômica (UE) ou União monetária (UM)\nUnião de integração total\nR: "))

if pergunta.upper() == "SIM":
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

pergunta = str(input("Inflação é o aumento contínuo e generalizado no índice de preços, e não podem ser confundidos com altas esporádicas de preços. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Moeda de curso forçado é aquela que é aceita pela economia por força de lei. Não possui valor em si própria, sendo necessário um decreto governamental garantindo o seu valor.\nDada tão afirmação julgue o texto a seguir VERDADEIRO ou FALSO.\n\nA moeda atualmente não tem lastro, sua aceitação é através de “curso forçado”.\nR: "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Julgue VERDADEIRO OU FALSO: RND = RN - T? "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Em: RND = RN - T\nO que significa T? "))

if pergunta.upper() == "TRIBUTAÇÃO":
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

pergunta = str(input("Em: RND = RN - T\nO que significa RND? "))

if pergunta.upper() == "RENDA NACIONAL DISPONÍVEL":
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

pergunta = str(input("Teoria macroeconômica trata-se de aspectos Ex-ante. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("Contabilidade Nacional ou Social tratam-se de aspectos Ex-post. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("O que significa BACEN? "))

if pergunta.upper() == "BANCO CENTRAL DO BRASIL":
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

pergunta = str(input("O que significa FMI? "))

if pergunta.upper() == "FUNDO MONETÁRIO INTERNACIONAL":
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

pergunta = str(input("O que significa CMN? "))

if pergunta.upper() == "CONSELHO MONETÁRIO NACIONAL":
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

pergunta = str(input("Sobre o conceito de economia julgue VERDAEIRO ou FALSO:\nEconomia é uma ciência social que estuda as necessidades humanas e a escassez de recursos buscando o equilíbrio.\nR: "))

if pergunta.upper() == "VERDADEIRO":
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

pergunta = str(input("A economia se divide em duas partes. Quais são elas? "))

if pergunta.upper() == "MACROECONOMIA E MICROECONOMIA" or pergunta.upper() == "MICROECONOMIA E MACROECONOMIA":
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

pergunta = str(input("Quais os agentes econômicos da MACROECONOMIA? (Formato: F, E, G e R): "))

if pergunta.upper() == "FAMÍLIAS, EMPRESAS, GOVERNO E RESTO DO MUNDO":
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

pergunta = str(input("Quais os agentes econômicos da MICROECONOMIA? "))

if pergunta.upper() == "EMPRESAS E FAMÍLIAS" or pergunta.upper() == "FAMÍLIAS E EMPRESAS":
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

pergunta = str(input("Custos de oportunidade é o custo que envolve desembolso monetário. Chamado também de custo explícito. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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

pergunta = str(input("Custos contábeis é o custo que não envolve desembolso monetário. Chamado também de custo implícito. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
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
porcentagem = (pontuacao / 45) * 100
porcentagem = float("{:.2f}".format(porcentagem))

print(f"Você acertou {porcentagem}% das perguntas ({pontuacao} de 45 perguntas)\nPontuação: {pontuacao} pontos\n")