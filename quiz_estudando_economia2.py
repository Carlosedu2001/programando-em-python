import os
from time import sleep
from msvcrt import getch

os.system("cls")

pontuacao = 0

pergunta = str(input("Indique quais os fatores que podem afetar a quantidade demandada de um bem, além do preço desse bem? (Formato: R, H, P): "))

if pergunta.upper() == "RENDA DOS CONSUMIDORES, HÁBITOS E PREFERÊNCIAS DOS CONSUMIDORES, PREÇO DE OUTROS BENS E SERVIÇOS CORRELACIONADOS" or pergunta.upper() == "RENDA DO CONSUMIDOR, HÁBITOS E PREFERÊNCIAS DO CONSUMIDOR, PREÇO DE OUTROS BENS E SERVIÇOS CORRELACIONADOS":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("No Monopólio, temos apenas uma empresa, não há barreiras a acesso de novas empresas. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Concorrência Monopolística, não difere da Concorrência Perfeita, nas condições de ingresso no mercado. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("No Oligopólio temos muitas empresas, barreiras a entrada de novos concorrentes. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Cartel está relacionado a Monopólio, não a Oligopólio. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("São agentes econômicos: O que e quanto produzir? Como produzir? Para quem produzir? (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("No sistema socialista esta presente a economia de mercado, diferentemente do sistema capitalista, onde predomina o órgão de planejamento. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Custo de oportunidade e custo contábil, não se diferem são idênticos. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Lei da Demanda: Permanecendo todas as outras variáveis iguais, à medida que o preço de um bem aumenta, a quantidade demandada por esse bem tende a diminuir. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("São problemas econômicos: O que e quanto produzir? Como produzir? Para quem produzir? (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("No sistema capitalista esta presente a economia de mercado, diferentemente do sistema socialista, onde predomina o órgão de planejamento. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Lei da Demanda: Permanecendo todas as outras variáveis iguais, à medida que o preço de um bem aumenta, a quantidade ofertada por esse bem tende a diminuir. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Lei da Oferta: Permanecendo todas as outras variáveis iguais, à medida que o preço de um bem aumenta a quantidade ofertada do bem também aumenta. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Estado é um agente econômico, que faz parte da MICROECONOMIA. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("A Terra é um fator de produção, que tem como remuneração o alugel. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("O Trabalho é um fator de produção, que tem como remuneração o salário. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("O Capital é um fator de produção, que tem como remuneração os juros. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("A Tecnologia é um fator de produção, que tem como remuneração os royalties. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("A Capacidade Empresarial é um fator de produção, que tem como remuneração o lucro. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Terra, Trabalho, Capital, Tecnologia e Capacidade Empresarial são fatores de remuneração. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Relacionado ao bem normal/superior julgue VERDADEIRO ou FALSO:\n\nRenda aumenta demanda pelo bem diminui.\nR: "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Relacionado ao bem saciado julgue VERDADEIRO ou FALSO:\n\nDemanda não é influenciada pela renda.\nR: "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Relacionado ao bem inferior julgue VERDADEIRO ou FALSO:\n\nRenda aumenta a demanda do bem também aumenta.\nR: "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Relacionado a externalidades julgue VERDADEIRO ou FALSO:\n\nExternalidades negativas: As ações de algum indivíduo ou empresa impõem custos a outro indivíduo ou empresa.\nExternalidades positivas: As ações de algum indivíduo ou empresa geram benefícios a outro indivíduo ou empresa.\nR: "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Renda dos consumidores sobe, quantidade demanda por bem inferior diminui. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Bem saciado não sofre interferência em quantidade demandada, quando preço diminui. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Lei da Oferta: Preço sobe quantidade ofertada sobe. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Equilíbrio é obtido pela interação das curvas da oferta e da demanda. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "VERDADEIRO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("O ponto de equilíbrio determina o custo e a quantidade de equilíbrio de um bem ou serviço. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

pergunta = str(input("Considerando: Quantidade ofertada: 5000 pç, quantidade demandada: 8000 pç, temos desequilíbrio de mercado com 3000 pç de excesso de oferta. (VERDADEIRO OU FALSO): "))

if pergunta.upper() == "FALSO":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(1)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    sleep(1)
    os.system("cls")

print("Processando pontuação...")
sleep(5)
os.system("cls")
porcentagem = (pontuacao / 30) * 100
porcentagem = float("{:.2f}".format(porcentagem))

print(f"Você acertou {porcentagem}% das perguntas ({pontuacao} de 30 perguntas)\nPontuação: {pontuacao} pontos\n")

getch()