try:
    from tkinter import *
except:
    from Tkinter import *
import random

root = Tk()
canvas = Canvas(root,width = 1000,height = 500,background = "black")
canvas.pack()

class Ball:
    def __init__(self):
        self.acceleration = [0,0]#this probably won't be used much but it is good to add one in any way
        self.velocity = [random.randint(2,6),random.randint(2,6)]# this will keep track of the speed in x and y
        self.position = [500,250]# this will keep track of the x and y position
        self.ball = canvas.create_rectangle(0,0,0,0)

    def updateVelocity(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

    def updatePosition(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0]>1000 or self.position[0]<0:
            self.velocity[0] = -self.velocity[0]
        if self.position[1]>500 or self.position[1]<0:
            self.velocity[1] = -self.velocity[1]

    def render(self):
        canvas.delete(self.ball)
        self.ball = canvas.create_rectangle(self.position[0]-5,self.position[1]-5,self.position[0]+5,self.position[1]+5,fill='white')

    def update(self):# this fuction will render the ball and update it's position and velocity
        self.updateVelocity()
        self.updatePosition()
        self.render()


class Paddle:
    def __init__(self,x):
        self.position = [x,250]
ball = Ball()
while True:
    ball.update()
    root.update()
