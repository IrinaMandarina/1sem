import turtle as tr
import numpy as np
tr.left(90)

def zero():
    for _ in range(2):
        tr.forward(50)
        tr.right(90)
        tr.forward(25)
        tr.right(90)
    tr.penup()
    tr.right(90)
    tr.forward(35)
    tr.left(90)
    tr.pendown()

def one():
    tr.penup()
    tr.forward(25)
    tr.right(45)
    tr.pendown()
    tr.forward(np.sqrt(2)*25)
    tr.right(135)
    tr.forward(50)
    tr.left(90)
    tr.penup()
    tr.forward(10)
    tr.left(90)
    tr.pendown()

def four():
    tr.penup()
    tr.forward(50)
    tr.pendown()
    tr.backward(25)
    tr.right(90)
    tr.forward(25)
    tr.left(90)
    tr.forward(25)
    tr.backward(50)
    tr.right(90)
    tr.penup()
    tr.forward(10)
    tr.left(90)
    tr.pendown()

def seven():
    tr.penup()
    tr.forward(50)
    tr.right(90)
    tr.pendown()
    tr.forward(25)
    tr.right(135)
    tr.forward(np.sqrt(2)*25)
    tr.left(45)
    tr.forward(25)
    tr.penup()
    tr.left(90)
    tr.forward(35)
    tr.left(90)
    tr.pendown()
    
def two():
    return None

def three():
    return None

def five():
    return None

def six():
    return None

def eight():
    return None

def nine():
    return None

b='144701'

def draw(c):
    for i in range(len(c)):
        if (c[i]=='0'): zero()
        if (c[i]=='1'): one()
        if (c[i]=='4'): four()
        if (c[i]=='7'): seven()

draw(b)