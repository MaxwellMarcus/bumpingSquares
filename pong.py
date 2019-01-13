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
        self.velocity = [random.randint(-6,6)/50,random.randint(-6,6)/50]# this will keep track of the speed in x and y
        while self.velocity[1] == 0 or self.velocity[0] == 0:
            self.velocity = [random.randint(-6,6)/50,random.randint(-6,6)/50]
        self.position = [500,250]# this will keep track of the x and y position
        self.ball = canvas.create_rectangle(0,0,0,0)
        self.paddle1 = Paddle(50,'arrows')
        self.paddle2 = Paddle(950,'ws')
        self.pause = True
    def updateVelocity(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

    def updatePosition(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if (abs(self.position[0]-self.paddle1.position[0])<6 and self.position[1] < self.paddle1.position[1]+50 and self.position[1] > self.paddle1.position[1]-50) or (abs(self.position[0]-self.paddle2.position[0])<6 and self.position[1] < self.paddle2.position[1]+50 and self.position[1] > self.paddle2.position[1]-50):
            self.velocity[0] = -self.velocity[0]*2
        if self.position[1]>500 or self.position[1]<0:
            self.velocity[1] = -self.velocity[1]

        if self.position[0] < 0 or self.position[0] > 1000:
            self.pause = True
            self.position = [500,250]
            self.paddle1.position[1] = 250
            self.paddle2.position[1] = 250
            self.velocity = [random.randint(-6,6)/50,random.randint(-6,6)/50]
            while self.velocity[1] == 0 or self.velocity[0] == 0:
                self.velocity = [random.randint(-6,6)/50,random.randint(-6,6)/50]
    def render(self):
        canvas.delete(self.ball)
        self.ball = canvas.create_rectangle(self.position[0]-5,self.position[1]-5,self.position[0]+5,self.position[1]+5,fill='white')

    def update(self):# this fuction will render the ball and update it's position and velocity
        self.updateVelocity()
        self.updatePosition()
        self.render()


class Paddle:
    def __init__(self,x,inputs):
        self.position = [x,250]
        self.paddle = canvas.create_rectangle(self.position[0],self.position[1]+50,self.position[0]-5,self.position[1]-50)
        if inputs == 'arrows':
            root.bind('<Up>',self.movePaddleUp)
            root.bind('<Down>',self.movePaddleDown)
        if inputs == 'ws':
            root.bind('w',self.movePaddleUp)
            root.bind('s',self.movePaddleDown)
    def movePaddleUp(self,event):
        self.position[1] -= 5
    def movePaddleDown(self,event):
        self.position[1] += 5
    def render(self):
        canvas.delete(self.paddle)
        self.paddle = canvas.create_rectangle(self.position[0],self.position[1]+50,self.position[0]-5,self.position[1]-50,fill='white')

ball = Ball()

def keyPress(event):
    if event.keysym == 'Escape':
        global game
        game = False
    if event.keysym == 'space':
        ball.update()
        ball.paddle1.render()
        ball.paddle2.render()
        ball.pause = not ball.pause

root.bind('<KeyPress>',keyPress)
game = True
ball.update()
ball.paddle1.render()
ball.paddle2.render()
while game:
    if not ball.pause:
        ball.update()
        ball.paddle1.render()
        ball.paddle2.render()
    root.update()
