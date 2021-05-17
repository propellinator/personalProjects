################################################################################
#
# Name: Carl Young
# Date: May 12th, 2021
# Project: Animation Practice
# Description: This is going to be where I practice animation on Python and
#   start to make a few games in the future.
#
################################################################################

# Libraries
from tkinter import *

def init(data):
    # Set 4
    '''data.row = data.height/10
    data.col = data.width/10
    data.margin = 5
    data.color = (-1,-1)'''
    # Set 3
    data.squareX = data.width/2
    data.squareY = data.height/2
    data.size = 10
    # Set 2
    '''data.circleCenters = []'''
    # Set 1
    '''data.circleSize = min(data.width,data.height)/10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = ""'''

def pointInGrid(x,y,data):
    return((data.margin <= x <= data.width-data.margin) and
           (data.margin <= y <= data.height-data.margin))

def getCell(x,y,data):
    if (not pointInGrid(x,y,data)):
        return (-1,-1)

def mousePressed(event,data):
    '''data.selectedX = event.x
    data.selectedY = event.y'''
    # Set 3
    data.size += 5
    # Set 2
    '''newCircleCenter = (event.x,event.y)
    data.circleCenters.append(newCircleCenter)'''
    # Set 1
    '''data.circleX = event.x
    data.circleY = event.y'''

def keyPressed(event,data):
    # Set 3
    if event.keysym == "Up":
        data.squareY -= 20
    elif event.keysym == "Down":
        data.squareY += 20
    elif event.keysym == "Right":
        data.squareX += 20
    elif event.keysym == "Left":
        data.squareX -= 20
    elif event.keysym == "s":
        data.size -= 5
    # Set 2
    '''if (event.char=="d"):
        if (len(data.circleCenters) > 0):
            data.circleCenters.pop(0)
        else:
            print("No more circles to delete!")'''
    # Set 1
    '''data.charText = event.char
    data.keysymText = event.keysym'''

def redrawAll(canvas,data):
    # Set 3
    canvas.create_text(data.width/2,20,
                       text="Example: Arrow Key Movement")
    canvas.create_text(data.width/2,40,
                       text="Pressing the arrow keys moves the square")
    canvas.create_text(data.width/2,60,
                       text="Click button-1 grows the square, 's' shrinks it")
    canvas.create_rectangle(data.squareX-data.size/2,data.squareY-data.size/2,
                            data.squareX+data.size/2,data.squareY+data.size/2,
                            fill="cyan")
    # Set 2
    '''for circleCenter in data.circleCenters:
        (cx,cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="cyan")
    canvas.create_text(data.width/2,20,
                       text="Example: Adding and Deleting Shapes")
    canvas.create_text(data.width/2,40,
                       text="Mouse clicks create circles")
    canvas.create_text(data.width/2,60,
                       text="Pressing 'd' deletes circles")'''
    # Set 1
    '''canvas.create_oval(data.circleX-data.circleSize,
                       data.circleY-data.circleSize,
                       data.circleX+data.circleSize,
                       data.circleY+data.circleSize)
    if data.charText != "":
        canvas.create_text(data.width/10,data.height/3,
                           text="char: "+data.charText)
    if data.keysymText != "":
        canvas.create_text(data.width/10,data.height*2/3,
                           text="keysym: "+data.keysymText)'''

def run(width=300, height=300):
    def redrawAllWrapper(canvas,data):
        canvas.delete(ALL)
        canvas.create_rectangle(0,0,data.width,data.height,fill="white",width=0)
        redrawAll(canvas,data)
        canvas.update()

    def mousePressedWrapper(event,canvas,data):
        mousePressed(event,data)
        redrawAllWrapper(canvas,data)

    def keyPressedWrapper(event,canvas,data):
        keyPressed(event,data)
        redrawAllWrapper(canvas,data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False,height=False)
    init(data)
    canvas = Canvas(root,width=data.width,height=data.height)
    canvas.configure(bd=0,highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>",lambda event: mousePressedWrapper(event,canvas,data))
    root.bind("<Key>",lambda event: keyPressedWrapper(event,canvas,data))
    redrawAll(canvas,data)
    root.mainloop()
    print("Bye!")

run(400,400)