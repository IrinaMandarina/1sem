import turtle as tr
import numpy as np
tr.speed(1)
def o(n,r):
    b=2*r*np.sin(np.pi/n)
    u=180-180*(n-2)/n
    tr.left(u/2)
    a=np.arange(0, n, 1)
    for i in a:
        tr.forward(b)
        tr.left(u)
    tr.right(u/2+90)
c=np.arange(3, 7, 1)
r=50
for n in c:
    o(n,r)
    r+=20
    tr.penup()
    tr.forward(10)
    tr.pendown()
    tr.left(90)
