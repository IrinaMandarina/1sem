import turtle as tr
def luch(n):
    for _ in range(n):
        tr.forward(50)
        tr.right(180)
        tr.forward(50)
        tr.left(180)
        tr.right(360/n)
luch(12)