import turtle as tr
def foo(n):
    k=5
    for _ in range(n):
        for _ in range(4):
            tr.right(90)
            tr.forward(k)
        k+=20
        tr.penup()
        tr.forward(10)
        tr.left(90)
        tr.forward(10)
        tr.right(90)
        tr.pendown()
foo(5)