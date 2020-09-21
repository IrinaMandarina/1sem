import turtle as tr
import numpy as np
tr.left(90)

b='0000'

def draw(c):
    for i in c:
        if (i=='0'): 
            q=open('zero.txt','r')
            s=q.readlines()
            for x in s: eval(x)
            q.close()
        if (i=='1'):
            w=open('one.txt','r')
            s=w.readlines()
            for x in s: eval(x)
            w.close()
        if (i=='4'):
            e=open('four.txt','r')
            s=e.readlines()
            for x in s: eval(x)
            e.close()
        if (i=='7'):
            r=open('seven.txt','r')
            s=r.readlines()
            for x in s: eval(x)
            r.close()

draw(b)