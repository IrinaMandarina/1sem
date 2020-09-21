from random import randint
import turtle

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.goto(-300,300)
turtle.goto(300,300)
turtle.goto(300,-300)
turtle.goto(-300,-300)
turtle.penup()

number_of_turtles = 5
dt=0.1
A=[] 
B=[]
vx=[]
vy=[]

pool = [turtle.Turtle(shape='turtle') for k in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    (x,y)=(randint(-200,200),randint(-200,200))
    unit.goto(x, y)
    A.append(x)
    B.append(y)
    vx.append(randint(0,10))
    vy.append(randint(0,10))


while True:
    for j in range(len(pool)):
        pool[j].goto(A[j],B[j])
        dx = vx[j]*dt
        dy = vy[j]*dt
        A[j] += dx
        B[j] += dy
        if (B[j]>300) or (B[j]<-300): vy[j] *= (-1)
        if (A[j]>300) or (A[j]<-300): vx[j] *= (-1)