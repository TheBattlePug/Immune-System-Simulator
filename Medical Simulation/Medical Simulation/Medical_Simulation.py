from graphics import *
from random import *
import time

windowHeight = 400
windowWidth = 600

win = GraphWin("Human Body", windowWidth, windowHeight)

class Cell:
    def __init__ (self, state, x, y):
        self.State = state
        self.X = x
        self.Y = y
   
class Pathogen:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    path = 0

def printPoint(x, y):
    print("(", x, ",", y, ")")

#Creates an array of pathogens that develope over time   
pathogenArray = []
pathogen = Pathogen(50, 100)
pathogenArray.append(pathogen)

p = Point(pathogen.X, pathogen.Y)
path = Circle(p, 5)
path.draw(win)
path.setFill('red')
pathogen.path = path

# Creates an array of a cells
cellAmount = 25
cellArray = []

for i in range(0, cellAmount):
    h = randrange(20, windowHeight-20)
    w = randrange(20, windowWidth-20)
    s = Cell("healthy", w, h)
    cellArray.append(s)


def tCell():
    global windowHeight
    global windowWidth

    x3 = -10
    y3 = 266
    tCell = Cell("healthy,", x3, x3)
    drawtCell = Circle(Point(tCell.X, tCell.Y), 8)
    drawtCell.draw(win)

    for i in range(0,20):
        x3 = x3 + 1

        drawtCell.undraw()
        drawtCell = Circle(Point(x3,y3), 8)
        drawtCell.setFill('blue')
        drawtCell.draw(win)
    
        

    while True:
        c1 = randrange(-10, 10)
        d1 = randrange(-10, 10)
        x3 = x3 + c1
        y3 = y3 + d1


        

        if (x3 > windowWidth):
            x3 = 0
             
        if (x3 < 0):
            x3 = windowWidth
             
        if (y3 > windowHeight):
            y3 = 0
                
        if (y3 < 0):
            y3 = windowHeight

        drawtCell.undraw()
        drawtCell = Circle(Point(x3,y3), 8)
        drawtCell.setFill('blue')
        drawtCell.draw(win)
        time.sleep(0.2)
        drawtCell.move(c1,d1)       
def bCell():
    global windowHeight
    global windowWidth

    x2 = -10
    y2 = 133
    bCell = Cell("healthy,", x2, y2)
    drawbCell = Circle(Point(bCell.X, bCell.Y), 15)
    drawbCell.draw(win)

    for i in range(0,20):
        x2 = x2 + 1


        drawbCell.undraw()
        drawbCell = Circle(Point(x2,y2), 15)
        drawbCell.setFill('yellow')
        drawbCell.draw(win)
        

    while True:
        a1 = randrange(-10, 10)
        b1 = randrange(-10, 10)
        x2 = x2 + a1
        y2 = y2 + b1


        if (x2 > windowWidth):
            x2 = 0
             
        if (x2 < 0):
            x2 = windowWidth
             
        if (y2 > windowHeight):
            y2 = 0
                
        if (y2 < 0):
            y2 = windowHeight


        drawbCell.undraw()
        drawbCell = Circle(Point(x2,y2), 15)
        drawbCell.setFill('yellow')
        drawbCell.draw(win)
        time.sleep(0.2)
        drawbCell.move(a1,b1)

def drawCell():
    
    x1 = pathogenArray[0].X
    y1 = pathogenArray[0].Y

    for i in range(0,len(cellArray)):
           cell = cellArray[i]
           drawCell = Circle(Point(cell.X, cell.Y), 10)
           drawCell.draw(win)

           if (abs(x1-cell.X)<=15 and abs(y1-cell.Y)<=15):
               cell.State = "infected"

           if (cell.State == "infected"):
               drawCell.undraw()
               drawCell = Circle(Point(cell.X, cell.Y), 10)
               drawCell.setOutline('red')
               drawCell.draw(win)
           
              
def movePathogen():
    
    for i in range(0, len(pathogenArray)):
        pathogen = pathogenArray[i]
 
        a = randrange(-10,20)
        newX = pathogen.X + a
        b = randrange(-10,20)      
        newY = pathogen.Y + b

        if (newX > windowWidth):
            newX = 0
             
        if (newX < 0):
            newX = windowWidth
             
        if (newY > windowHeight):
            newY = 0
                
        if (newY < 0):
            newY = windowHeight
        
        path = pathogen.path;
        path.undraw()
        path = Circle(Point(newX,newY), 5)
        path.setFill('red')
        path.draw(win)
        pathogen.path = path
        pathogen.X = newX
        pathogen.Y = newY



def draw():
    

    while True:
         movePathogen()
         drawCell()
         time.sleep(0.2)
         
         

draw()

