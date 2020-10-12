import pygame
from pygame.draw import *
from random import randint

gamer_name = input('What is your name?')

pygame.init()

FPS = 20
screen = pygame.display.set_mode((600, 450))


def new_ball(screen_ball: pygame.Surface, x_ball: int, y_ball: int, r_ball: int, color_ball: tuple) -> None:
    """
    Function draws a usual ball. It costs 1 coin.
    @param screen_ball: pygame.Surface of the game display
    @param x_ball: x-coordinate of the ball's center
    @param y_ball: y-coordinate of the ball's center
    @param r_ball: radius of the ball
    @param color_ball: color of the ball
    """
    circle(screen_ball, color_ball, (x_ball, y_ball), r_ball)


def money_ball(screen_m_ball: pygame.Surface, x_m_ball: int, y_m_ball: int) -> None:
    """
    Function draws a specific 'money' ball. It costs 5 coins.
    @param screen_m_ball: pygame.Surface of the game display
    @param x_m_ball: x-coordinate of the ball's center
    @param y_m_ball: y-coordinate of the ball's center
    """
    circle(screen_m_ball, color_m_ball, (x_m_ball, y_m_ball), r_m_ball)
    line(screen_m_ball, color_m_lines, (x_m_ball, y_m_ball - r_m_ball), (x_m_ball, y_m_ball + r_m_ball), 2)
    line(screen_m_ball, color_m_lines, (x_m_ball - r_m_ball, y_m_ball), (x_m_ball + r_m_ball, y_m_ball), 2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0  # score counter
balls = []  # list of coordinates and other characteristics of usual balls
m_balls = []  # list of coordinates and other characteristics of money balls
timer = 0  # 'time' of the game

r_m_ball = 10  # radius of money ball
color_m_ball = (255, 215, 0)  # color of money ball
color_m_lines = (139, 69, 19)  # lines' color of money ball

# event queue
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x_mouse, y_mouse) = event.pos  # coordinates of the mouse
            # condition for hitting the ball
            for ball in balls:
                if (ball[0] - x_mouse) ** 2 + (ball[1] - y_mouse) ** 2 <= ball[2] ** 2:
                    k += 1  # counting of score
                    balls.remove(ball)  # disappearance of the shot ball
            for m_ball in m_balls:
                if (m_ball[0] - x_mouse) ** 2 + (m_ball[1] - y_mouse) ** 2 <= r_m_ball ** 2:
                    k += 5  # counting of score
                    m_balls.remove(m_ball)  # disappearance of the shot ball

    # output of the score on the game display
    f = pygame.font.Font(None, 36)
    text = f.render('Score:' + str(k), 1, (180, 0, 0))
    screen.blit(text, (250, 20))

    # movement of usual balls
    for ball in balls:
        ball[0] += ball[4]
        ball[1] += ball[5]
        # conditions of reflection from the walls
        if (ball[0] + ball[2] > 600) or (ball[0] - ball[2] < 0):
            ball[4] *= -1
        if (ball[1] + ball[2] > 450) or (ball[1] - ball[2] < 0):
            ball[5] *= -1
        # condition for disappearing if the ball is old
        if ball[6] < 150 and not ball[7]:
            new_ball(screen, ball[0], ball[1], ball[2], ball[3])
            ball[6] += 1
        else:
            del ball

    # movement of money balls
    for m_ball in m_balls:
        m_ball[0] += m_ball[2]
        m_ball[1] += m_ball[3]
        m_ball[3] += 1
        # conditions of reflection from the walls
        if (m_ball[0] + r_m_ball > 600) or (m_ball[0] - r_m_ball < 0):
            m_ball[2] *= -1
        if (m_ball[1] + r_m_ball > 450) or (m_ball[1] - r_m_ball < 0):
            m_ball[3] *= -1
        # condition for disappearing if the ball is old
        if m_ball[4] < 100 and not m_ball[5]:
            money_ball(screen, m_ball[0], m_ball[1])
            m_ball[4] += 1
        else:
            del m_ball

    # appearance of a new ball
    if timer % 20 == 0:
        x = randint(100, 500)
        y = randint(100, 350)
        r = randint(10, 100)
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        lifetime = 0
        click = False
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        balls.append([x, y, r, color, dx, dy, lifetime, click])
        new_ball(screen, x, y, r, color)

    # appearance of a new money ball
    if timer % 40 == 0:
        x_m = randint(100, 500)
        y_m = randint(100, 350)
        dx_m = 2 * randint(-2, 5)
        dy_m = 2 * randint(-5, 5)
        lifetime = 0
        click = False
        m_balls.append([x_m, y_m, dx_m, dy_m, lifetime, click])
        money_ball(screen, x_m, y_m)

    timer += 1  # counting time of the game
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((0, 0, 0))  # updating the display

pygame.quit()

new_gamer = [gamer_name, k]
gamers = []  # list of gamers and their scores

# building of the list of gamers
with open('gamers.txt', 'r+') as file:
    for s in file:  # reading from the file
        gamers.append(s.split())
    gamers.append(new_gamer)
    for gamer in gamers:
        gamer[1] = int(gamer[1])
    gamers = sorted(gamers, key=lambda gamer: gamer[1], reverse=True)  # sorting of records
    file.seek(0)  # clearing of the file
    file.truncate()
    for gamer in gamers:
        gamer = str(gamer[0]) + ' ' + str(gamer[1]) + '\n'
        file.write(gamer)  # rewriting of the file
