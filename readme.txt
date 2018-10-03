from tkinter import *
import random

root = Tk()
canvas = Canvas(root,height = 100,width = 100)
canvas.pack()

class One:
    def __init__(self):
        self.one = canvas.create_oval(38.5,38.5,62.5,62.5,fill = "red")
class Two:
    def __init__(self):
        self.one = canvas.create_oval(10,10,35,35,fill = "red")
        self.two = canvas.create_oval(65, 65, 90, 90, fill="red")
class Three:
    def __init__(self):
        self.one = canvas.create_oval(0,0,25,25,fill = "red")
        self.two = canvas.create_oval(38.5,38.5, 62.5,62.5, fill="red")
        self.three = canvas.create_oval(75, 75, 100, 100, fill="red")

class Four:
    def __init__(self):
        self.one = canvas.create_oval(0, 0, 25, 25, fill="red")
        self.two = canvas.create_oval(0,75, 25, 100, fill="red")
        self.three = canvas.create_oval(75, 75, 100, 100, fill="red")
        self.four = canvas.create_oval(100,0, 75, 25, fill="red")

class Five:
    def __init__(self):
        self.one = canvas.create_oval(0, 0, 25, 25, fill="red")
        self.two = canvas.create_oval(0, 75, 25, 100, fill="red")
        self.three = canvas.create_oval(75, 75, 100, 100, fill="red")
        self.four = canvas.create_oval(100, 0, 75, 25, fill="red")
        self.five = canvas.create_oval(38.5,38.5, 62.5,62.5, fill="red")

class Six:
    def __init__(self):
        self.one = canvas.create_oval(0, 0, 25, 25, fill="red")
        self.two = canvas.create_oval(0, 75, 25, 100, fill="red")
        self.three = canvas.create_oval(75, 75, 100, 100, fill="red")
        self.four = canvas.create_oval(100, 0, 75, 25, fill="red")
        self.five = canvas.create_oval(0,38.5, 25,62.5, fill="red")
        self.six = canvas.create_oval(100,38.5, 75,62.5, fill="red")

def roll(event):
    canvas.delete(ALL)
    num = random.randint(1,6)
    if num == 1:
        one = One()
    elif num == 2:
        two = Two()
    elif num == 3:
        three = Three()
    elif num == 4:
        four = Four()
    elif num == 5:
        five = Five()
    elif num == 6:
        six = Six()
root.bind("<Key>",roll)
root.mainloop()
