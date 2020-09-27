import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((230,230,255))

pygame.draw.circle(screen, (255, 211, 0), [200, 200], 100)
pygame.draw.circle(screen, (255, 0, 0), [250, 180], 20)
pygame.draw.circle(screen, (255, 0, 0), [150, 180], 30)
pygame.draw.circle(screen, (0, 0, 0), [250, 180], 10)
pygame.draw.circle(screen, (0, 0, 0), [150, 180], 20)
pygame.draw.rect(screen, (0, 0, 0), (150, 250, 100, 10))
pygame.draw.polygon(screen, (0, 0, 0), [(230, 170), (230, 150), (310,120), (310, 130)])
pygame.draw.polygon(screen, (0, 0, 0), [(170, 160), (170, 140), (90,120), (90, 130)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()