__author__ = 'grahamcooke'

import tkinter
import random
import logging

logger = logging.getLogger()
logging.basicConfig(level = logging.DEBUG)

def generate():
    l = [0 for x in range(8)]
    l[0] = vary(10)
    l[1] = vary(20)
    l[2] = vary(50)
    l[3] = vary(100)
    l[4] = vary(500)
    l[5] = vary(1000)
    l[6] = vary(10000)
    l[7] = vary(100000)

    for x in range(8):
        g[x]["text"] = str(int(l[x]))
        g[x].pack()

def vary(base):
    base = base + (base * (random.randint(-5,5)/10))
    return base

def makeCode():
    d["text"] = randCode()
    return

def randCode():
    l = ''
    for i in range(8):
        v = random.randint(0,63)
        n = code[v]
        l = l+n

    return l

code = {a:b for a,b in zip(range(64),"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!")}
logger.debug(code)


root = tkinter.Tk()

root.wm_minsize(width = 500, height = 400)
root.wm_maxsize(width = 500, height = 600)

b = tkinter.Button(root, text = "Generate Grist Drops", command = generate)
b.pack()
q = tkinter.Button(root, text = "Quit", command = root.destroy)
q.pack(side = "bottom")
c = tkinter.Button(root, text = "New Captcha Code", command = makeCode)
c.pack()

d = tkinter.Label(root)
d.pack()

g = [tkinter.Label(root) for x in range(8)]
for x in range(8):
    g[x].pack()

root.mainloop()