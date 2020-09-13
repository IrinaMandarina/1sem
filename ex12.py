import turtle as tr
import numpy as np
tr.left(90)
def o(k):
    a=np.arange(0,k)
    for _ in a:
        for _ in range(180):
            tr.forward(3)
            tr.right(1)
        for _ in range(180):
            tr.forward(1)
            tr.right(1)
o(6)