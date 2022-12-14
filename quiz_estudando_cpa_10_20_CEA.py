import os
from time import sleep
from msvcrt import getch
import matplotlib.pyplot as plt

vertical = [0, 0, 2]
horizontal = [0, 1, 2.5]
plt.plot(horizontal, vertical)

os.system("cls")

pontuacao = 0

pergunta = str(input("""Podemos afirmar que são atribuições do CNSP - Conselho Nacional de Seguros Privados:
\nI - Disciplinar a corretagem do mercado e a profissão de corretor.
II - Estabelecer as diretrizes gerais das operações de resseguro.
III - Fixar as diretrizes e normas da política de seguros privados.
IV - Controlar e fiscalizar os mercados de seguro.
\nEstá incorreto o que se afirma em:
\na) I e III, apenas.
b) I, II e III, apenas.
c) IV, apenas.
d) I, II, III e IV.\n\n"""))

if pergunta.upper() == "C":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mC\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Fabricio é um investidor conservador e gosta de emprestar seu dinheiro para o governo através dos Títulos Públicos Federais. Ele deseja aplicar em um título prefixado que não tenha risco de reinvestimento. Neste caso, a indicação adequada de título para este cliente é:
\na) NTN-F.
b) LTN.
c) LFT.
d) NTN-B.\n\n"""))

if pergunta.upper() == "B":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mB\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""O PIB representa a soma de todos os bens e serviços __________, em um(a) __________, durante certo período de tempo.
\na) Intermediários / País
b) Finais / Região
c) Finais / País
d) Intermediários / Empresa\n\n"""))

if pergunta.upper() == "B":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mB\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Tag along pode ser definido como:
\na) Extensão do prêmio de cintrole. Direito conferido aos acionistas minoritários em caso de alienação de ações realizadas pelos controles da companhia. Oferta mínima de 80%.
b) Aumento da quantidade de ações, ocasionando redução do valor da ação.
c) Redução da quantidade de ações, ocasionando aumento do valor da ação.
d) É o direito que possuem os atuais acionistas de subscrever o aumento de capital na mesma proporção de sua participação no capital da companhia.\n\n"""))

if pergunta.upper() == "A":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mA\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Os fundos de renda fixa curto prazo aplicam seus recursos em:
\na) Títulos Públicos Federais ou privados indexados à taxa de juros ou índice de preço, com prazo máximo de 375 dias e prazo médio da carteira do fundo inferior a 60 dias.
b) Títulos Públicos Federais ou privados indexados à taxa de juros ou índice de preço, com prazo máximo de 365 dias e prazo médio da carteira de 60 dias.
c) Títulos Públicos Federais ou privados indexados à taxa de juros ou índice de preço, com prazo máximo de 365 dias e prazo médio da carteira do fundo inferior a 60 dias.
d) Títulos Públicos Federais indexados à taxa de juros ou índice de preço, com prazo máximo de 365 dias e prazo médio da carteira do fundo inferior a 60 dias.\n\n"""))

if pergunta.upper() == "A":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mA\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Ebitda (earnings before interest, taxes, depreciation and amortization) é um indicador muito utilizado para avaliar empresas de capital aberto.
Podemos dizer que a melhor definição sobre EBITDA é:
\na) Lucro antes das despesas de juros.
b) Lucro antes das despesas de juros, impostos e depreciação.
c) Lucro antes das despesas de juros, impostos, depreciação e amortização.
d) Nenhuma das alternativas.\n\n"""))

if pergunta.upper() == "C":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mC\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Um lançador de uma opção de venda, caso seja exercida, terá a obrigação de:
\na) Comprar ações ao preço de exercício.
b) Vender ações pelo preço de exercício.
c) Comprar ações pelo preço de mercado.
d) Vender ações pelo preço de mercado.\n\n"""))

if pergunta.upper() == "A":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mA\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Arnaldo tem um plano de previdência VGBL e decidiu transformar o saldo acumulado em renda mensal por prazo certo no valor de R$ 4.000,00, por 180 meses. Após 80 meses, Arnaldo veio a falecer. Com base nesse relato, podemos afirmar que a renda:
\na) Foi extinta imediatamente com o falecimento do titular.
b) Será paga ao beneficiário indicado por mais 100 meses.
c) Será concluído o pagamento do benefício somente até o final do ano vigente.
d) Será extinta, tendo em vista que o titular usufruiu de todo o benefício em vida.\n\n"""))

if pergunta.upper() == "B":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mB\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

pergunta = str(input("""Analise os títulos listados a seguir e assinale a alternativa correta.
\t __________________________________
\t|      Ativo      |     Rating     |
\t ----------------------------------
\t|     Título 1    |      CCC       |
\t ----------------------------------
\t|     Título 2    |       BB       |
\t ----------------------------------
\t|     Título 3    |       A        |
\t ----------------------------------
\t|     Título 4    |       DD       |
\t ----------------------------------
\na) O título 1 tem um risco de crédito maior do que o título 4, por isso podemos esperar uma maior rentabilidade.
b) O título 2 tem maior risco de crédito se comparado ao título 3, por isso podemos esperar uma rentabilidade maior.
c) O título 4 aplica os recursos apenas em títulos soberanos e, por isso, tende a ter menor rentabilidade e menor risco.
d) O título 3 é o mais arriscado, por isso podemos esperar uma rentabilidade maior.\n\n"""))

if pergunta.upper() == "B":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mB\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

plt.show()
pergunta = str(input(f"""O gráfico apresentado representa:
\na) O Titular de uma opção de compra
b) O Lançador de uma opção de compra
c) O Titular de uma opção de venda
d) O Lançador de uma opção de venda\n\n"""))

if pergunta.upper() == "A":
    print("\033[4;34;32mCorreta a resposta\033[m")
    sleep(3)
    os.system("cls")
    pontuacao += 1
elif pergunta.upper() == 'SAIR':
    exit()
else:
    print("\033[4;31;40mResposta incorreta\033[m")
    print("\n\nResposta correta: \033[4;34;32mA\033[m\n\nPressione qualquer tecla para continuar")
    getch()
    os.system("cls")

print("Processando pontuação...")
sleep(5)
os.system("cls")
porcentagem = (pontuacao / 10) * 100
porcentagem = float("{:.2f}".format(porcentagem))

print(f"Você acertou {porcentagem}% das perguntas ({pontuacao} de 10 perguntas)\nPontuação: {pontuacao} pontos\n")

print("Pressione qualquer tecla para continuar")
getch()