import turtle as tr
import numpy as np
def o(k):
    a=np.arange(1, k+1)
    for n in a:
        for i in range(360):
            tr.forward(n)
            tr.right(1)
        for _ in range(360):
            tr.forward(n)
            tr.left(1)
o(6)