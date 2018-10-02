# bumpgame
from tkinter import *
import random

root = Tk()
canvas = Canvas(root,width = 2000,height = 1000,background = "black")
canvas.pack()

square1X = random.randint(0,1000)
square1Y = random.randint(0,1000)

square2X = random.randint(0,1000)
square2Y = random.randint(0,1000)

incrementerY1 = 11
incrementerX1 = 10
incrementerY2 = 11
incrementerX2 = 10

increment1X = 10
increment1Y = 10
increment2X = 10
increment2Y = 10

square1 = canvas.create_rectangle(square1X - 50,square1Y - 50,square1X + 50,square1Y + 50,fill = "blue")
square2 = canvas.create_rectangle(square2X - 50,square2Y - 50,square2X + 50,square2Y + 50,fill = "red")


while True:
    canvas.delete(ALL)
    square1Y += increment1Y
    square1X += increment1X
    square2Y += increment2Y
    square2X += increment2X

    if  square1Y > root.winfo_height() - 50:
        increment1Y = -incrementerY1
    elif square1Y < 50:
        increment1Y = incrementerY1
    if square1X > root.winfo_width() - 50:
        increment1X = -incrementerX1
    elif square1X < 50:
        increment1X = incrementerX1

    if  square2Y > root.winfo_height() - 50:
        increment2Y = -incrementerY2
    elif square2Y < 50:
        increment2Y = incrementerY2
    if square2X > root.winfo_width() - 50:
        increment2X = -incrementerX2
    elif square2X < 50:
        increment2X = incrementerX2

    if square2X + 50 > square1X - 50 and square2X + 50 < square1X +50 and square2Y + 50 < square1Y + 100 and square2Y + 50 > square1Y - 50:
        increment1X = incrementerX1
        increment2X = - incrementerX2

    if square2X - 50 < square1X + 50 and square2X - 50 > square1X - 50 and square2Y + 50 < square1Y + 100 and square2Y + 50 > square1Y - 50:
        increment1X = - incrementerX1
        increment2X = incrementerX2

    if square2Y + 50 > square1Y - 50 and square2Y + 50 < square1Y +50 and square2X+ 50 < square1X+ 100 and square2X + 50 > square1X - 50:
        increment1Y = incrementerY1
        increment2Y = - incrementerY2

    if square2Y - 50 < square1Y + 50 and square2Y - 50 > square1Y - 50 and square2X + 50 < square1X + 100 and square2X + 50 > square1X - 50:
        increment1Y = -incrementerY1
        increment2Y = incrementerY2
    square1 = canvas.create_rectangle(square1X - 50, square1Y - 50, square1X + 50, square1Y + 50, fill="blue")
    square2 = canvas.create_rectangle(square2X - 50, square2Y - 50, square2X + 50, square2Y + 50, fill="red")


    #incrementerY2 += .01
    #incrementerY1 += .01
    #incrementerX2 += .01
    #incrementerX1 += .01
    root.update()
