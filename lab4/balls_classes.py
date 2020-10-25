import pygame
from pygame.draw import *
from random import randint

gamer_name = input('What is your name?')

pygame.init()

FPS = 20
screen = pygame.display.set_mode((600, 450))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k = 0  # score counter
balls = []  # list of coordinates and other characteristics of usual balls
m_balls = []  # list of coordinates and other characteristics of money balls
timer = 0  # 'time' of the game

r_m_ball = 20  # radius of money ball
color_m_ball = (255, 215, 0)  # color of money ball
color_m_lines = (139, 69, 19)  # lines' color of money ball


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, r, color, dx, dy, lifetime, screen, click):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        self.lifetime = lifetime
        self.screen = screen
        self.click = click

    def new_ball(self):
        """
        Function draws a usual ball. It costs 1 coin.
        """
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def new_money_ball(self):
        """
        Function draws a specific 'money' ball. It costs 5 coins.
        """
        circle(self.screen, self.color, (self.x, self.y), self.r)
        line(self.screen, color_m_lines, (self.x, self.y - r_m_ball), (self.x, self.y + r_m_ball), 2)
        line(self.screen, color_m_lines, (self.x - r_m_ball, self.y), (self.x + r_m_ball, self.y), 2)

    def movement_ball(self):
        self.x += self.dx
        self.y += self.dy
        # conditions of reflection from the walls
        if (self.x + self.r > 600) or (self.x - self.r < 0):
            self.dx *= -1
        if (self.y + self.r > 450) or (self.y - self.r < 0):
            self.dy *= -1

    def movement_money_balls(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 1
        # conditions of reflection from the walls
        if (self.x + r_m_ball > 600) or (self.x - r_m_ball < 0):
            m_ball.dx *= -1
        if (self.y + r_m_ball > 450) or (self.y - r_m_ball < 0):
            self.dy *= -1


# event queue
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x_mouse, y_mouse) = event.pos  # coordinates of the mouse
            # condition for hitting the ball
            for ball in balls:
                if (ball.x - x_mouse) ** 2 + (ball.y - y_mouse) ** 2 <= ball.r ** 2:
                    k += 1  # counting of score
                    ball.click = True  # disappearance of the shot ball
            for m_ball in m_balls:
                if (m_ball.x - x_mouse) ** 2 + (m_ball.y - y_mouse) ** 2 <= r_m_ball ** 2:
                    k += 5  # counting of score
                    m_ball.click = True  # disappearance of the shot ball

    # output of the score on the game display
    f = pygame.font.Font(None, 36)
    text = f.render('Score:' + str(k), 1, (180, 0, 0))
    screen.blit(text, (250, 20))

    for i in range(len(balls)):  # interaction of the balls
        for j in range(i+1, len(balls)):
            x_next1 = balls[i].dx + balls[i].x
            x_next2 = balls[j].dx + balls[j].x
            y_next1 = balls[i].dy + balls[i].y
            y_next2 = balls[j].dy + balls[j].y
            if ((balls[i].x - balls[j].x) ** 2 + (balls[i].y - balls[j].y) ** 2 <= (balls[i].r + balls[j].r) ** 2) and \
                    ((balls[i].x - balls[j].x) ** 2 + (balls[i].y - balls[j].y) ** 2 > (x_next1 - x_next2) ** 2 + (y_next1 - y_next2) ** 2):
                balls[i].dx *= (-1)
                balls[j].dx *= (-1)
                balls[i].dy *= (-1)
                balls[j].dy *= (-1)

    # movement of usual balls
    for ball in balls:
        ball.movement_ball()
        # condition for disappearing if the ball is old
        if ball.lifetime > 0 and not ball.click:
            ball.new_ball()
            ball.lifetime -= 1
        else:
            balls.remove(ball)

    # appearance of a new ball
    if timer % 30 == 0:
        r = randint(10, 100)
        x = randint(100, 500)
        y = randint(100, 350)
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        lifetime = 100
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        click = False
        ball = Ball(x, y, r, color, dx, dy, lifetime, screen, click)
        balls.append(ball)
        ball.new_ball()

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
