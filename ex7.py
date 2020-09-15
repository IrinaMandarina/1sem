import turtle as tr
import numpy as np
tr.speed(10)
v=np.arange(0, 360, 0.1)
for i in v:
    x=i*np.cos(i*np.pi/180)
    y=i*np.sin(i*np.pi/180)
    tr.goto(x,y)