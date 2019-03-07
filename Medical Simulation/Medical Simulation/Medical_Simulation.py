from graphics import *
from random import *
import time

windowHeight = 400
windowWidth = 400

win = GraphWin("Human Body", windowHeight, windowWidth)

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



