import numpy as np
import turtle as tr
tr.speed(0)
def o(n):
    for _ in range(int(n/2)):
        for _ in range(360):
            tr.forward(1)
            tr.right(1)
        for _ in range(360):
            tr.forward(1)
            tr.left(1)
        tr.left(360/n)
n=6
o(n)