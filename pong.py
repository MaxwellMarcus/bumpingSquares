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
        self.velocity = [random.randint(-6,6)/10,random.randint(-6,6)/10]# this will keep track of the speed in x and y
        while abs(self.velocity[1]) < .04 or abs(self.velocity[0]) < .04:
            self.velocity = [random.randint(-6,6)/10,random.randint(-6,6)/10]
        self.position = [500,250]# this will keep track of the x and y position
        self.ball = canvas.create_rectangle(0,0,0,0)
        self.line = canvas.create_line(500,0,500,500,width=5,fill='white')
        self.paddle1 = Paddle(50,'ws')
        self.paddle2 = Paddle(950,'arrows')
        self.pause = True
    def updateVelocity(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

    def updatePosition(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if (abs(self.position[0]-self.paddle1.position[0])<6 and self.position[1] < self.paddle1.position[1]+20 and self.position[1] > self.paddle1.position[1]-20) or (abs(self.position[0]-self.paddle2.position[0])<6 and self.position[1] < self.paddle2.position[1]+20 and self.position[1] > self.paddle2.position[1]-20):
            self.velocity[0] = -self.velocity[0]*(random.randint(8,25)/10)
        if self.position[1]>500 or self.position[1]<0:
            self.velocity[1] = -self.velocity[1]

        if self.position[0] < 0 or self.position[0] > 1000:
            if self.position[0] < 0:
                self.paddle2.score += 1
            else:
                self.paddle1.score += 1
            self.pause = True
            self.position = [500,250]
            self.paddle1.position[1] = 250
            self.paddle2.position[1] = 250
            self.paddle1.render()
            self.paddle2.render()
            self.velocity = [random.randint(-6,6)/10,random.randint(-6,6)/10]
            while abs(self.velocity[1]) < .04 or abs(self.velocity[0]) < .04:
                self.velocity = [random.randint(-6,6)/10,random.randint(-6,6)/10]
    def render(self):
        canvas.delete(self.ball)
        canvas.delete(self.line)
        self.line = canvas.create_line(500,0,500,500,width=5,fill='white')
        self.ball = canvas.create_rectangle(self.position[0]-5,self.position[1]-5,self.position[0]+5,self.position[1]+5,fill='white')

    def update(self):# this fuction will render the ball and update it's position and velocity
        self.updateVelocity()
        self.updatePosition()
        self.render()


class Paddle:
    def __init__(self,x,inputs):
        self.position = [x,250]
        self.paddle = canvas.create_rectangle(self.position[0],self.position[1]+50,self.position[0]-5,self.position[1]-50)
        self.scoreText = canvas.create_text(0,0)
        self.score = 0
        if inputs == 'arrows':
            root.bind('<Up>',self.movePaddleUp)
            root.bind('<Down>',self.movePaddleDown)
        if inputs == 'ws':
            root.bind('w',self.movePaddleUp)
            root.bind('s',self.movePaddleDown)
    def movePaddleUp(self,event):
        if self.position[1] > 20:
            self.position[1] -= 10
    def movePaddleDown(self,event):
        if self.position[1] < 480:
            self.position[1] += 10
    def render(self):
        global start
        canvas.delete(self.paddle)
        canvas.delete(self.scoreText)
        self.paddle = canvas.create_rectangle(self.position[0],self.position[1]+20,self.position[0]-10,self.position[1]-20,fill='white')
        if start:
            if self.position[0]  > 500:
                self.scoreText = canvas.create_text(self.position[0]-200,50,text=str(self.score),fill='white',font=('TkTextFont',100))
            else:
                self.scoreText = canvas.create_text(self.position[0]+200,50,text=str(self.score),fill='white',font=('TkTextFont',100))


ball = Ball()
game = True
start = False
def keyPress(event):
    global game,start
    if event.keysym == 'Escape':
        if not start:
            game = False
        else:
            start = False
    if event.keysym == 'space':
        start = True
        ball.paddle1.position[1] = 250
        ball.paddle2.position[1] = 250
        ball.position = [500,250]
        ball.update()
        ball.paddle1.render()
        ball.paddle2.render()
        ball.pause = False
def startScreen():
    canvas.delete(ALL)
    canvas.create_text(500,250,text='PONG',fill='white',font=('TkTextFont',100))
    canvas.create_text(500,400,text='Press space to start \nPlayer on the left uses w and s to move \nplayer on the right uses the arrows to move', fill='white',font=('TkTextFont',25))
    ball.paddle1.render()
    ball.paddle2.render()
    root.update()

root.bind('<KeyPress>',keyPress)

ball.update()
ball.paddle1.render()
ball.paddle2.render()

while game:
    if not start:
        startScreen()
        canvas.delete(ALL)
    if start:
        if not ball.pause:
            ball.update()
            ball.paddle1.render()
            ball.paddle2.render()
        root.update()
