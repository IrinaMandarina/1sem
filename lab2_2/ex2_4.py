import turtle as tr
import numpy as np
vx=7
vy=5
a=-3
dt=0.1
f=1
(x,y)=(0,50)
while True:
    tr.goto(x,y)
    dx = vx*dt
    dy = vy*dt + a*(dt**2)/2
    x += dx
    y += dy
    vy += a*dt
    if (y<0):
        vy *=(-1)