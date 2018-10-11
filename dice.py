from tkinter import *
import random

root = Tk()

canvas = Canvas(root,width = 800,height = 800)
canvas.pack()

def circle(x,y,radius,fill):
    canvas.create_oval(x - radius,y - radius,x + radius,y + radius,fill = fill)

class Dice:
    def __init__(self):
        self.sides = 6
    def roll(self):
        self.num = 5#random.randint(1,self.sides)
        print(self.num)
        if self.num % 2 == 1:
            self.size = 800/((self.num - 1)/2)
        else:
            self.size = 800/(self.num/2)
        i = 0
        while i < self.num:
            canvas.create_line(0,self.size * i,800,self.size*i,width = 10)
            if i == 0 and self.num % 2 == 1:
                circle(400,400,50,fill = "black")

            elif (self.num - i )% 2 == 0:
                circle(self.size/2,self.size/4 + self.size*((i/2)) + self.size/4,self.size/8,"black")

            elif (self.num - i )% 2 == 1:
                circle(800 - self.size/2,800 - (self.size/4 + self.size*((i/2))) + self.size/4 + 0,self.size/8,"black")
            i += 1
dice = Dice()
dice.roll()

root.mainloop()
