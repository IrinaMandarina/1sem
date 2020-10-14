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
        self.rect = pygame.Rect((x-r, y-r), (2*r, 2*r))
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

    '''group = balls
    hits = []
    for ball in balls:
        group.remove(ball)
        hits = pygame.sprite.spritecollide(ball, group, True)
        for hit in hits:
            hit.dx *= (-1)
            hit.dy *= (-1)
            ball.dx *= (-1)
            ball.dy *= (-1)'''

    '''for i in range(len(balls)-1):
        for j in range(i+1, len(balls)):
            if pygame.sprite.collide_rect(balls[i], balls[j]):
                balls[i].dx *= (-1)
                balls[i].dy *= (-1)
                balls[j].dx *= (-1)
                balls[j].dy *= (-1)'''

    # movement of usual balls
    for ball in balls:
        ball.movement_ball()
        # condition for disappearing if the ball is old
        if ball.lifetime > 0 and not ball.click:
            ball.new_ball()
            ball.lifetime -= 1
        else:
            del ball

    # movement of money balls
    for m_ball in m_balls:
        m_ball.movement_money_balls()
        # condition for disappearing if the ball is old
        if m_ball.lifetime > 0 and not m_ball.click:
            m_ball.new_money_ball()
            m_ball.lifetime -= 1
        else:
            del m_ball

    # appearance of a new ball
    if timer % 20 == 0:
        r = randint(10, 100)
        x = randint(100, 500)
        '''flag = True
        while flag:
            x = randint(100, 500)
            flag = False
            for ball in balls:
                if (ball.x + ball.r >= x - r) or (ball.x - ball.r >= x + r):
                    flag = True'''
        y = randint(100, 350)
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        lifetime = 100
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        click = False
        ball = Ball(x, y, r, color, dx, dy, lifetime, screen, click)
        balls.append(ball)
        ball.new_ball()

    # appearance of a new money ball
    if timer % 40 == 0:
        x_m = randint(100, 500)
        y_m = randint(100, 350)
        dx_m = 2 * randint(-2, 5)
        dy_m = 2 * randint(-5, 5)
        lifetime = 150
        click = False
        m_ball = Ball(x_m, y_m, r_m_ball, color_m_ball, dx_m, dy_m, lifetime, screen, click)
        m_balls.append(m_ball)
        m_ball.new_money_ball()

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
