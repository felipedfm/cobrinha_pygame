#iniciando o pygame
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#variaveis
altura = 640
largura = 640
x_cobra = int(altura/2)
y_cobra = int(largura/2)
x_maca = randint(40, 600)
y_maca = randint(50, 430)
vel = 8
x_controle = vel
y_controle = 0
pontos = 0
morreu = False
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('Fantasy', 40, True, True)
    #tela
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('jogo')
lista_corpo = []
comprimento_inicial = 5
def aumenta_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela,(0,155,0),(XeY[0], XeY[1], 30, 30))


def reiniciar():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_corpo, lista_cabeca, x_maca, y_maca, vel, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(altura / 2)
    y_cobra = int(largura / 2)
    lista_corpo = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    vel = 8
    morreu = False


while True:
    fps.tick(30)
    tela.fill((255,255,255))
    msg = f'pontos: {pontos}'
    texto_formatado = fonte.render(msg, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #controles

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == vel:
                    pass
                else:
                    x_controle = - vel
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -vel:
                    pass
                else:
                    x_controle = +vel
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = - vel
            if event.key == K_DOWN:
                if y_controle == -vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = + vel
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
   # if pygame.key.get_pressed()[K_a]:
     #   x_cobra = x_cobra-20
    #if pygame.key.get_pressed()[K_d]:
      #  x_cobra = x_cobra+20
    #if pygame.key.get_pressed()[K_w]:
     #   y_cobra = y_cobra-20
    #if pygame.key.get_pressed()[K_s]:
     #   y_cobra = y_cobra+20



    #obj player
    cobra = pygame.draw.rect(tela, (0,155,0),(x_cobra,y_cobra,30,30))



#obj maça
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 30, 30))
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 600)
        pontos += 1
        comprimento_inicial += 2
        vel += 0.5

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_corpo.append(lista_cabeca)
    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Fantasy', 30, True, False)
        msg = 'GAME OVER pressione R para jogar novamente'
        texto_formatado = fonte2.render(msg, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0


    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]
    aumenta_cobra(lista_corpo)


 #fps e texto na tela
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
