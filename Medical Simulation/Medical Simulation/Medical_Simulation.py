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

def printPoint(x, y):
    print("(", x, ",", y, ")")


x1 = 50
y1 = 100
pathogen1 = Pathogen(x1, y1)

# Creates a matrix of a defined height and width
h = 6
w = 6;
Matrix = [[Cell("healthy", randrange(20, windowHeight-20),randrange(20, windowWidth-20)) for x in range(h)] for y in range(w)] 

def healing():
    global windowHeight
    global windowWidth

    x2 = -10
    y2 = 133
    bCell = Cell("healthy,", x2, y2)
    drawbCell = Circle(Point(bCell.X, bCell.Y), 15)
    drawbCell.draw(win)

    x3 = -10
    y3 = 266
    tCell = Cell("healthy,", x3, x3)
    drawtCell = Circle(Point(tCell.X, tCell.Y), 8)
    drawtCell.draw(win)

    time.sleep(5)
    for i in range(0,20):
        x2 += 1
        x3 += 1


        drawbCell.undraw()
        drawbCell = Circle(Point(x2,y2), 15)
        drawbCell.setFill('yellow')
        drawbCell.draw(win)
        drawbCell.move(a1,b1)

        drawtCell.undraw()
        drawtCell = Circle(Point(x3,y3), 8)
        drawtCell.setFill('blue')
        drawtCell.draw(win)
        drawtCell.move(c1,d1)
    
        

    while True:
        a1 = randrange(-10, 10)
        b1 = randrange(-10, 10)
        c1 = randrange(-10, 10)
        d1 = randrange(-10, 10)
        x2 = x2 + a1
        y2 = y2 + b1
        x3 = x3 + c1
        x4 = x4 + d1


        if (x2 > windowWidth):
            x2 = 0
             
        if (x2 < 0):
            x2 = windowWidth
             
        if (y2 > windowHeight):
            y2 = 0
                
        if (y2 < 0):
            y2 = windowHeight

        if (x3 > windowWidth):
            x3 = 0
             
        if (x3 < 0):
            x3 = windowWidth
             
        if (y3 > windowHeight):
            y3 = 0
                
        if (y3 < 0):
            y3 = windowHeight

        drawbCell.undraw()
        drawbCell = Circle(Point(x2,y2), 15)
        drawbCell.setFill('yellow')
        drawbCell.draw(win)
        time.sleep(0.2)
        drawbCell.move(a1,b1)

        drawtCell.undraw()
        drawtCell = Circle(Point(x3,y3), 8)
        drawtCell.setFill('blue')
        drawtCell.draw(win)
        time.sleep(0.2)
        drawtCell.move(c1,d1)
    
       




def drawCell():
    global x1
    global x2
    for i in range(0,h):
        for j in range(0,w):
           cell = Matrix[i][j]
           drawCell = Circle(Point(cell.X, cell.Y), 10)
           drawCell.draw(win)

           if (abs(x1-cell.X)<=15 and abs(y1-cell.Y)<=15):
               cell.State = "infected"

           if (cell.State == "infected"):
               drawCell.undraw()
               drawCell = Circle(Point(cell.X, cell.Y), 10)
               drawCell.setOutline('red')
               drawCell.draw(win)
              


def draw():
    global x1
    global y1
    global pathogen1
        
    p = Point(pathogen1.X, pathogen1.Y)
    path = Circle(p, 5)
    path.draw(win)
    path.setFill('red')

    while True:
         a = randrange(-10,20)
         x1 = x1 + a
         b = randrange(-10,20)      
         y1 = y1 + b

         if (x1 > windowWidth):
             x1 = 0
             
         if (x1 < 0):
             x1 = windowWidth
             
         if (y1 > windowHeight):
             y1 = 0
                
         if (y1 < 0):
             y1 = windowHeight
         
         path.undraw()
         path = Circle(Point(x1,y1), 5)
         path.setFill('red')
         path.draw(win)

         drawCell()
         time.sleep(0.2)
         path.move(a,b)
         printPoint(x1,y1)

         

draw()


