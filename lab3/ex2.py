import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

def clouds(a):
    x=randint(-220,600)
    y=randint(0,250)
    pygame.draw.ellipse(screen, (a, a, a), (x, y, 220, 50))

def nlo(x,y):
    treu = pygame.Surface((int(240), int(150)))
    treu.fill((255, 255, 255))
    treu.set_colorkey((255, 255, 255))
    pygame.draw.polygon(treu, (250, 250, 250), [(int(125), 0), (int(240), int(150)), (int(10), int(150))])
    treu.set_alpha(100)
    screen.blit(treu, (x, y))
    pygame.draw.ellipse(screen, (190, 190, 190), (x, y ,250, 75))
    pygame.draw.ellipse(screen, (230, 230, 230), (x+30, y-15 ,190, 60))
    pygame.draw.ellipse(screen, (253, 233, 16), (x+110, y+50 ,30, 18))
    pygame.draw.ellipse(screen, (253, 233, 16), (x+60, y+45 ,30, 18))
    pygame.draw.ellipse(screen, (253, 233, 16), (x+160, y+45 ,30, 18))
    pygame.draw.ellipse(screen, (253, 233, 16), (x+15, y+30 ,30, 18))
    pygame.draw.ellipse(screen, (253, 233, 16), (x+210, y+30 ,30, 18))

def alien(x,y):
    surprise=(randint(128, 255), randint(0, 128), 0)
    pygame.draw.ellipse(screen, (187, 240, 51), (x+10, y+35, 50, 105)) #body
    pygame.draw.ellipse(screen, (187, 255, 51), (x-20, y+40, 40, 40))  #left arm
    pygame.draw.ellipse(screen, (187, 255, 51), (x-32, y+70, 25, 25))
    pygame.draw.ellipse(screen, (187, 255, 51), (x-25, y+90, 20, 20))
    pygame.draw.ellipse(screen, (187, 255, 51), (x+57, y+40, 40, 40))  #right arm
    pygame.draw.ellipse(screen, (187, 255, 51), (x+80, y+70, 25, 25))
    pygame.draw.ellipse(screen, (187, 255, 51), (x+98, y+85, 25, 17))
    pygame.draw.circle(screen, surprise, [x+130, y+80], 22)  #apple
    pygame.draw.line(screen, (0, 0, 0), [x+135, y+65], [x+140, y+50], 2)
    pygame.draw.polygon(screen, (0, 230, 0), [(x+136, y+54), (x+148, y+45), (x+142,y+50)])
    pygame.draw.ellipse(screen, (187, 255, 51), (x-5, y+110, 40, 40))  #left leg
    pygame.draw.ellipse(screen, (187, 255, 51), (x-10, y+140, 30, 30))
    pygame.draw.ellipse(screen, (187, 255, 51), (x-12, y+160, 20, 20))
    pygame.draw.ellipse(screen, surprise, (x-10, y+180, 27, 15))
    pygame.draw.ellipse(screen, (187, 255, 51), (x+40, y+110, 40, 40))  #right leg
    pygame.draw.ellipse(screen, (187, 255, 51), (x+50, y+140, 30, 30))
    pygame.draw.ellipse(screen, (187, 255, 51), (x+48, y+160, 20, 20))
    pygame.draw.ellipse(screen, surprise, (x+50, y+180, 27, 15))
    image  = pygame.image.load('head.png')  #head
    image.set_colorkey((255, 255, 255))
    image_rect=image.get_rect(topleft=(x-53, y-90))
    screen.blit(image, image_rect)
    pygame.draw.circle(screen, (187, 255, 51), [x-20, y-60], 12)  #left corn
    pygame.draw.circle(screen, surprise, [x-30, y-75], 8)
    pygame.draw.circle(screen, (187, 255, 51), [x+30, y-78], 12)  #left corn
    pygame.draw.circle(screen, surprise, [x+25, y-96], 8)

pygame.draw.polygon(screen, (0, 51, 102), [(0, 0), (600, 0), (600, 400), (0, 400)])
pygame.draw.polygon(screen, (18, 53, 36), [(0, 400), (600, 400), (600,700), (0, 700)])
pygame.draw.circle(screen, (253, 245, 230), [250, 100], 60)

for _ in range(20): 
    x=randint(100, 230)
    clouds(x)

nlo(40, 300)
alien(400, 400)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()