# bumpgame
from tkinter import *

root = Tk()
canvas = Canvas(root,width = 2000,height = 1000,background = "black")
canvas.pack()

square1X = 150
square1Y = 150

square2X = 500
square2Y = 500

incrementerY = 10
incrementerX = 10

increment1X = 1
increment1Y = 1
increment2X = 1
increment2Y = 1

square1 = canvas.create_rectangle(square1X - 50,square1Y - 50,square1X + 50,square1Y + 50,fill = "blue")
square2 = canvas.create_rectangle(square2X - 50,square2Y - 50,square2X + 50,square2Y + 50,fill = "red")


while True:
    canvas.delete(ALL)
    square1Y += increment1Y
    square1X += increment1X
    square2Y += increment2Y
    square2X += increment2X

    if  square1Y > root.winfo_height() - 50:
        increment1Y = -incrementerY
    elif square1Y < 50:
        increment1Y = incrementerY
    if square1X > root.winfo_width() - 50:
        increment1X = -incrementerX
    elif square1X < 50:
        increment1X = incrementerX

    if  square2Y > root.winfo_height() - 50:
        increment2Y = -incrementerY
    elif square2Y < 50:
        increment2Y = incrementerY
    if square2X > root.winfo_width() - 50:
        increment2X = -incrementerX
    elif square2X < 50:
        increment2X = incrementerX

    if square1X - 50 < square2X + 50 and square1X > square2X and square1Y :
        increment1X = incrementerX
        increment2X = - incrementerX
    square1 = canvas.create_rectangle(square1X - 50, square1Y - 50, square1X + 50, square1Y + 50, fill="blue")
    square2 = canvas.create_rectangle(square2X - 50, square2Y - 50, square2X + 50, square2Y + 50, fill="red")
