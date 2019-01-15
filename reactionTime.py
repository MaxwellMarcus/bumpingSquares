try:
    from tkinter import *
except:
    from Tkinter import *
import random
import time

root = Tk()
canvas = Canvas(root,width = 1000,height = 500,background = "black")
canvas.pack()

def hit(event):
    global hitted,game
    if not event.keysym == 'Escape':
        hitted = True
    else:
        game = False

root.bind('<KeyPress>',hit)
hitted = False
game = True
going = False
times = []
best = 100000000
worst = 0
print('hit a key when you see the box, try to get the fastest possible time')
while game:
    if not going and random.randint(1,100000) == 37:
        canvas.create_rectangle(480,230,520,270,fill='white')
        going = True
        timer = time.time()
    if hitted and not going:
        hitted = False
    if hitted and going:
        hitted = False
        going = False
        canvas.delete(ALL)
        if time.time()-timer < best:
            best = time.time()-timer
        if time.time()-timer > worst:
            worst = time.time()-timer
        times.append(time.time()-timer)
        print(time.time()-timer)

    root.update()
avg = 0
for i in times:
    avg += i
avg /= len(times)
print('your average time was ' + str(avg) + ', nice job!')
print('your best time was ' + str(best) + '!')
print('your worst time was ' + str(worst))
