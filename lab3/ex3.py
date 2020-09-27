import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

def nlo(x,y,k):
    treu = pygame.Surface((int(240*k), int(150*k)))
    treu.fill((255, 255, 255))
    treu.set_colorkey((255, 255, 255))
    pygame.draw.polygon(treu, (250, 250, 250), [(int(125*k), 0), (int(240*k), int(150*k)), (int(10*k), int(150*k))])
    treu.set_alpha(100)
    screen.blit(treu, (x, y))
    pygame.draw.ellipse(screen, (190, 190, 190), (x, y ,int(250*k), int(75*k)))
    pygame.draw.ellipse(screen, (230, 230, 230), (int(x+30*k), int(y-15*k), int(190*k), int(60*k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x+110*k), int(y+50*k), int(30*k), int(18*k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x+60*k), int(y+45*k) ,int(30*k), int(18*k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x+160*k), int(y+45*k),int(30*k), int(18*k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x+15*k), int(y+30*k) ,int(30*k), int(18*k)))
    pygame.draw.ellipse(screen, (253, 233, 16), (int(x+210*k), int(y+30*k) ,int(30*k), int(18*k)))

def alien(x ,y ,k, m):
    al = pygame.Surface((int(600), int(700)))
    al.fill((255, 255, 255))
    al.set_colorkey((255, 255, 255))
    surprise=(randint(128, 255), randint(0, 128), 0)
    pygame.draw.ellipse(al, (187, 240, 51), (x, y, int(k*50), int(k*105))) #body
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-30*k), int(y+5*k), int(k*40), int(k*40)))  #left arm
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-42*k), int(y+35*k), int(k*25), int(k*25)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-35*k), int(y+55*k), int(k*20), int(k*20)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+47*k), int(y+5*k), int(k*40), int(k*40)))  #right arm
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+70*k), int(y+35*k), int(k*25), int(k*25)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+88*k), int(y+50*k), int(k*25), int(k*17)))
    pygame.draw.circle(al, surprise, [int(x+120*k), int(y+45*k)], int(k*22))  #apple
    pygame.draw.line(al, (0, 0, 0), [int(x+125*k), int(y+30*k)], [int(x+130*k), int(y+15*k)], 2)
    pygame.draw.polygon(al, (0, 230, 0), [(int(x+126*k), int(y+19*k)), (int(x+138*k), int(y+10*k)), (int(x+132*k),int(y+15*k))])
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-15*k), int(y+75*k), int(k*40), int(k*40)))  #left leg
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-20*k), int(y+105*k), int(k*30), int(k*30)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x-22*k), int(y+125*k), int(k*20), int(k*20)))
    pygame.draw.ellipse(al, surprise, (int(x-20*k), int(y+145*k), int(k*27), int(k*15)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+30*k), int(y+75*k), int(k*40), int(k*40)))  #right leg
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+40*k), int(y+105*k), int(k*30), int(k*30)))
    pygame.draw.ellipse(al, (187, 255, 51), (int(x+38*k), int(y+125*k), int(k*20), int(k*20)))
    pygame.draw.ellipse(al, surprise, (int(x+40*k), int(y+145*k), int(k*27), int(k*15)))
    image  = pygame.image.load('head.png')  #head
    image.set_colorkey((255, 255, 255))
    image = pygame.transform.scale(image, (int(150*k), int(146*k)))
    image_rect=image.get_rect(topleft=(int(x-63*k), int(y-125*k)))
    al.blit(image, image_rect)
    pygame.draw.circle(al, (187, 255, 51), [int(x-30*k), int(y-95*k)], int(k*12))  #left corn
    pygame.draw.circle(al, surprise, [int(x-40*k), int(y-110*k)], int(k*8))
    pygame.draw.circle(al, (187, 255, 51), [int(x+20*k), int(y-113*k)], int(k*12))  #left corn
    pygame.draw.circle(al, surprise, [int(x+15*k), int(y-131*k)], int(k*8))
    if (m==-1): al = pygame.transform.flip(al, True,False)
    screen.blit(al, (0, 0))

pygame.draw.polygon(screen, (0, 51, 102), [(0, 0), (600, 0), (600, 400), (0, 400)])
pygame.draw.polygon(screen, (18, 53, 36), [(0, 400), (600, 400), (600,700), (0, 700)])

pygame.draw.circle(screen, (253, 245, 230), [450, 100], 60)  #moon

image  = pygame.image.load('clouds2.jpg')  #sky
image.set_colorkey((255, 255, 255))
image = pygame.transform.scale(image, (600, 400))
image_rect=image.get_rect()
image.set_alpha(100)
screen.blit(image, image_rect)

nlo(40, 300, 1)
nlo(400, 400, 0.7)
nlo(70, 450, 0.8)
alien(300, 400, 1, 1)
alien(450, 500, 0.8, 1)
alien(450, 600, 0.5, -1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()