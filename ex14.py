import turtle as tr
def star(n):
    u=180-180/n
    for _ in range(n):
        tr.forward(100)
        tr.left(u)
star(11)