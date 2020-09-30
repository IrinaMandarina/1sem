# 10 image
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((450, 610))

SKY = (0, 235, 247)
GRASS = (2, 250, 15)
SUN = (250, 217, 2)
TRUNK = (189, 189, 189)
TRUNK_CONTUR = (237, 197, 128)
LEAVES = (47, 161, 48)
LEAVES_CONTUR = (36, 255, 105)
APPLE = (255, 188, 173)
UNICORN = (255, 250, 232)
UNICORN_EYE = (251, 0, 255)
MANE_1 = (162, 161, 255)
MANE_2 = (130, 189, 245)
MANE_3 = (222, 154, 237)
MANE_4 = (130, 245, 237)

screen.fill(SKY)
pygame.draw.rect(screen, GRASS, (0, 300, 450, 310))  # grass


def tree(screen_tree: pygame.Surface, x: int, y: int, a: float) -> None:
    """

    Function draws a tree.
    screen - pygame.Surface of the image.
    (x,y) - coordinates of top left corner of a trunk.
    a - coefficient of compression.
    """
    pygame.draw.rect(screen_tree, TRUNK, (x, y, int(30 * a), int(150 * a)))  # trunk
    pygame.draw.rect(screen_tree, TRUNK_CONTUR, (x, y, int(30 * a), int(150 * a)), 2)

    pygame.draw.ellipse(screen_tree, LEAVES,
                        (int(x - 40 * a), int(y - 20 * a), int(110 * a), int(100 * a)))  # down block of leaves
    pygame.draw.ellipse(screen_tree, LEAVES_CONTUR, (int(x - 40 * a), int(y - 20 * a), int(110 * a), int(100 * a)), 2)

    pygame.draw.ellipse(screen_tree, LEAVES,
                        (int(x - 50 * a), int(y - 200 * a), int(130 * a), int(200 * a)))  # top block of leaves
    pygame.draw.ellipse(screen_tree, LEAVES_CONTUR, (int(x - 50 * a), int(y - 200 * a), int(130 * a), int(200 * a)), 2)

    pygame.draw.ellipse(screen_tree, LEAVES,
                        (int(x - 90 * a), int(y - 100 * a), int(200 * a), int(110 * a)))  # central block of leaves
    pygame.draw.ellipse(screen_tree, LEAVES_CONTUR, (int(x - 90 * a), int(y - 100 * a), int(200 * a), int(110 * a)), 2)

    pygame.draw.ellipse(screen_tree, APPLE, (int(x - 55 * a), int(y - 30 * a), int(20 * a), int(20 * a)))  # left apple
    pygame.draw.ellipse(screen_tree, APPLE,
                        (int(x - 10 * a), int(y - 100 * a), int(20 * a), int(20 * a)))  # central apple
    pygame.draw.ellipse(screen_tree, APPLE, (int(x + 45 * a), int(y - 150 * a), int(20 * a), int(20 * a)))  # top apple
    pygame.draw.ellipse(screen_tree, APPLE, (int(x + 20 * a), y, int(20 * a), int(20 * a)))  # down apple


def unicorn(main_screen: pygame.Surface, x_0: int, y_0: int, a: float, boo: bool) -> None:
    """

    Function draws a unicorn.
    main_screen - pygame.Surface of the image.
    (x_0,y_0) - coordinates of top left corner of an image.
    a - coefficient of compression.
    boo - mirror rotation indicator. If boo=False, unicorn will turn left.
    """
    screen_unicorn = pygame.Surface((int(250 * a), int(320 * a)))
    screen_unicorn.fill((255, 255, 255))
    screen_unicorn.set_colorkey((255, 255, 255))

    (x, y) = (int(50 * a), int(180 * a))

    pygame.draw.ellipse(screen_unicorn, UNICORN, (x, y, int(170 * a), int(80 * a)))  # body
    pygame.draw.ellipse(screen_unicorn, UNICORN,
                        (int(x + 100 * a), int(y - 70 * a), int(100 * a), int(33 * a)))  # nose
    pygame.draw.ellipse(screen_unicorn, UNICORN,
                        (int(x + 100 * a), int(y - 85 * a), int(70 * a), int(50 * a)))  # head

    pygame.draw.ellipse(screen_unicorn, UNICORN_EYE,
                        (int(x + 133 * a), int(y - 73 * a), int(18 * a), int(15 * a)))  # eye
    pygame.draw.ellipse(screen_unicorn, (0, 0, 0), (int(x + 143 * a), int(y - 70 * a), int(7 * a), int(7 * a)))  # pupil
    pygame.draw.ellipse(screen_unicorn, UNICORN,
                        (int(x + 137 * a), int(y - 70 * a), int(7 * a), int(3 * a)))  # blik

    pygame.draw.polygon(screen_unicorn, (130, 164, 245),
                        [(int(x + 140 * a), int(y - 83 * a)), (int(x + 140 * a), int(y - 170 * a)),
                         (int(x + 125 * a), int(y - 83 * a))])  # corn
    pygame.draw.rect(screen_unicorn, UNICORN,
                     (int(x + 100 * a), int(y - 50 * a), int(50 * a), int(100 * a)))  # neck

    pygame.draw.rect(screen_unicorn, UNICORN,
                     (int(x + 137 * a), int(y + 30 * a), int(11 * a), int(100 * a)))  # right leg
    pygame.draw.rect(screen_unicorn, UNICORN,
                     (int(x + 107 * a), int(y + 40 * a), int(13 * a), int(100 * a)))  # central right leg
    pygame.draw.rect(screen_unicorn, UNICORN,
                     (int(x + 60 * a), int(y + 33 * a), int(12 * a), int(100 * a)))  # central left leg
    pygame.draw.rect(screen_unicorn, UNICORN,
                     (int(x + 25 * a), int(y + 37 * a), int(13 * a), int(100 * a)))  # left leg

    pygame.draw.ellipse(screen_unicorn, MANE_1,
                        (int(x + 85 * a), int(y - 80 * a), int(35 * a), int(15 * a)))  # mane
    pygame.draw.ellipse(screen_unicorn, MANE_2, (int(x + 95 * a), int(y - 90 * a), int(40 * a), int(18 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x + 90 * a), int(y - 85 * a), int(30 * a), int(13 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_4, (int(x + 80 * a), int(y - 74 * a), int(25 * a), int(17 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_1, (int(x + 70 * a), int(y - 70 * a), int(35 * a), int(15 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_2, (int(x + 65 * a), int(y - 55 * a), int(35 * a), int(20 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x + 70 * a), int(y - 60 * a), int(33 * a), int(15 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_4, (int(x + 70 * a), int(y - 35 * a), int(35 * a), int(10 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x + 68 * a), int(y - 18 * a), int(40 * a), int(25 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_1, (int(x + 48 * a), int(y - 7 * a), int(60 * a), int(15 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_2, (int(x + 69 * a), int(y - 29 * a), int(37 * a), int(25 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x + 72 * a), int(y - 32 * a), int(50 * a), int(15 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_1, (int(x + 68 * a), int(y - 42 * a), int(40 * a), int(17 * a)))

    pygame.draw.ellipse(screen_unicorn, MANE_1,
                        (int(x - 10 * a), int(y + 10 * a), int(50 * a), int(25 * a)))  # tail
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x - 20 * a), int(y + 25 * a), int(40 * a), int(18 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_2, (int(x - 25 * a), int(y + 35 * a), int(43 * a), int(19 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x - 23 * a), int(y + 47 * a), int(50 * a), int(25 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_4, (int(x - 27 * a), int(y + 62 * a), int(45 * a), int(19 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_1, (int(x - 30 * a), int(y + 75 * a), int(52 * a), int(25 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_3, (int(x - 43 * a), int(y + 90 * a), int(43 * a), int(20 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_4, (int(x - 30 * a), int(y + 95 * a), int(48 * a), int(25 * a)))
    pygame.draw.ellipse(screen_unicorn, MANE_2, (int(x - 35 * a), int(y + 107 * a), int(43 * a), int(15 * a)))

    if not boo:
        screen_unicorn = pygame.transform.flip(screen_unicorn, True, False)
    main_screen.blit(screen_unicorn, (x_0, y_0))


def sun(main_screen: pygame.Surface, x_0: int, y_0: int, r_0: int) -> None:
    """

    Function draws the sun.
    main_screen - pygame.Surface of the image.
    (x_0, y_0) - coordinates of top left corner of the image.
    r_0 - radius of the sun.
    """
    (x, y) = (x_0, y_0)
    for r in range(2 * r_0, 0, -2):
        scr = pygame.Surface((r, r))
        scr.fill((0, 0, 0))
        scr.set_colorkey((0, 0, 0))
        pygame.draw.circle(scr, SUN, (int(0.5 * r), int(0.5 * r)), int(0.5 * r))
        scr.set_alpha(3)
        x += 1
        y += 1
        main_screen.blit(scr, (x, y))


sun(screen, 200, 20, 150)
tree(screen, 50, 300, 0.5)
tree(screen, 100, 250, 0.75)
tree(screen, 150, 300, 0.57)
tree(screen, 20, 350, 1)
tree(screen, 70, 400, 0.5)
unicorn(screen, 150, 270, 1, True)
unicorn(screen, 200, 170, 0.5, False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
