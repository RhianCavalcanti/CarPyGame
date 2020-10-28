import pygame
from random import randint
pygame.init()
x = 380     # max 530 min min 230 era 380
y = 100       #era 100
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 2500
timer = 0
tempo_segundo = 0

velocidade_outros = 12
velocidade = 10

#gráfico
fundo = pygame.image.load('fundo.png')
carro = pygame.image.load('carrop1.png')
policia = pygame.image.load('policia1.png')
ambulancia = pygame.image.load('ambulancia1.png')
camionete = pygame.image.load('caminhonete1.png')
vocebateu= pygame.image.load('vocebateu.png')

#musica
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
somcolisao= pygame.mixer.Sound('somcolisao1.ogg')

#placar
font = pygame.font.SysFont('arial black',30)
texto = font.render("Score: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

#define o tamanho da janela
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("CarPyGame")

#janela
janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x<= 520:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 230:
        x -= velocidade

    #verifica a colisao
    if ((x + 80 > pos_x and y + 180 > pos_y) ): #colisão direita
        y = 1200


    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)): #colisão esquerda
        y = 1200

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c))and((x - 80 < pos_x - 136 and y + 180 > pos_y_c)): #colisão central
        y = 1200

    #posição dos carros após passarem pela tela
    if (pos_y <= -80):
        pos_y = randint(800,1000)

    if (pos_y_a <= -80):
        pos_y_a = randint(1200, 2000)

    if (pos_y_c <= -80):
        pos_y_c = randint(2200, 3000)

    #timer
    if (timer <20):
        timer +=1
    else:
        if y != 1200:
            tempo_segundo += 1
            texto = font.render("Score: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
            timer = 0
        if y == 1200:
            tempo_segundo = tempo_segundo
            texto = font.render("Score: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
            timer = 0
    #controle da velocidade dos outros carros
    pos_y  -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10  

    #posição dos objetos na tela
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(ambulancia, (pos_x - 300, pos_y_a))
    janela.blit(camionete, (pos_x - 136, pos_y_c))
    janela.blit(texto,pos_texto)

    #condição para som da colisão
    colisao=1
    if y==1200 and somcolisao.get_num_channels()!=8: #condicional para o efeito sonoro 'somcolisao' não ficar em looping
        somcolisao.play(0)
    if y==1200:
        janela.blit(vocebateu, (50, 70)) #fiz outra condicional para a 'colisaotela' aparecer e não sair
        pygame.mixer.music.stop()

    pygame.display.update()
pygame.quit()
