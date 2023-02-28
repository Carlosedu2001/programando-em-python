import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Definindo o tamanho da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Definindo a fonte do jogo
fonte = pygame.font.SysFont(None, 50)

# Definindo o texto do jogo
texto = fonte.render("Encontre o Tesouro!", True, BRANCO)

# Definindo a posição do texto na tela
posicao_texto = texto.get_rect(center=(LARGURA_TELA/2, ALTURA_TELA/5))

# Definindo a posição do tesouro na tela
posicao_tesouro = pygame.Rect(random.randint(0, LARGURA_TELA-50), random.randint(0, ALTURA_TELA-50), 50, 50)

# Loop principal do jogo
jogando = True
while jogando:
    # Verificando eventos do Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jogando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Verificando se o jogador clicou no tesouro
            if posicao_tesouro.collidepoint(pygame.mouse.get_pos()):
                # Caso tenha clicado no tesouro, mostra mensagem de vitória
                mensagem = fonte.render("Parabéns, você encontrou o tesouro!", True, VERMELHO)
                posicao_mensagem = mensagem.get_rect(center=(LARGURA_TELA/2, ALTURA_TELA/2))
                tela.blit(mensagem, posicao_mensagem)
                pygame.display.update()
                pygame.time.wait(1500)
                # Gera nova posição para o tesouro
                posicao_tesouro = pygame.Rect(random.randint(0, LARGURA_TELA-50), random.randint(0, ALTURA_TELA-50), 50, 50)
            else:
                # Caso tenha clicado fora do tesouro, mostra mensagem de erro
                mensagem = fonte.render("Ops, tente novamente!", True, AZUL)
                posicao_mensagem = mensagem.get_rect(center=(LARGURA_TELA/2, ALTURA_TELA/2))
                tela.blit(mensagem, posicao_mensagem)
                pygame.display.update()
                pygame.time.wait(800)

    # Preenchendo a tela com a cor preta
    tela.fill(PRETO)

    # Desenhando o texto na tela
    tela.blit(texto, posicao_texto)

    # Desenhando o tesouro na tela
    pygame.draw.rect(tela, VERMELHO, (posicao_tesouro[0], posicao_tesouro[1], 50, 50))

    # Atualizando a tela
    pygame.display.update()

# Finalização do Pygame
pygame.quit()