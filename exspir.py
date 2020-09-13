import numpy as np
import turtle as tr
tr.speed (10)
k=0.001
n=8
v=np.arange(0, 360*n, 1)
for i in v:
    u=i*np.pi/180
    tr.forward(0.5*k*(u*(1+u**2)**0.5 + np.log(u+(1+u**2)**0.5)))
    tr.left(1)