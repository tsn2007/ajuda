import pygame
from pygame import *
from sys import exit
pygame.init()

relogio=pygame.time.Clock()

largura=1920
altura=1015

tela=pygame.display.set_mode((largura, altura))

fonte=pygame.font.SysFont('arial', 100, True, False)
fonte2=pygame.font.SysFont('arial', 500,True,False)

fundo= pygame.image.load('dfundo.png')
pirete=pygame.image.load('pitete.PNG')

pygame.display.set_caption('600%')

def fim():
    while(True):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        frase=str('PERDESTE O TEU TEMPO TOMA ! XD')
        frase_fim=fonte.render(frase,True, (255,255,255))

        tela.blit(fundo, (0,0))
        tela.blit(frase_fim, (50,50))
        tela.blit( pirete, (400, 200) )
        pygame.display.update()

def menu():
    while (True):

        tela.blit( fundo, (0, 0) )

        relogio.tick( 1 )

        segundos=pygame.time.get_ticks()/1000
        segundos2 = round( segundos )
        segundos_f=round( segundos )
        segundos3=str('{}%'.format(segundos_f))
        contador=fonte2.render(segundos3,True,(255,255,255))
        tela.blit(contador,(300,200))

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        if segundos2 == 10 :
            menu2()
            pygame.display.update()

def menu2():
    while (True):
        tela.blit(fundo,(0,0))
        continuar=fonte.render('Clique na tela para continuar!', True,(255,255,255))
        tela.blit(continuar,(250,400))
        for event in pygame.event.get():
            if event.type ==MOUSEBUTTONDOWN:
                fim()
        pygame.display.update()

menu()

