from graphics import *
from random import *
import time

win = GraphWin("Human Body", 200, 200)

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

#def infectCells():
 #   global drawhealthyCell
  #  global healthyCell

   # if (x1 >= 55):
    #          drawhealthyCell.undraw()
     #         drawhealthyCell = Circle(Point(healthyCell.X, healthyCell.Y), 10)
         #     drawhealthyCell.setOutline('red')
          #    drawhealthyCell.draw(win)
           #   healthyCell.State = "infected"
    #print("The cells are now ")

def drawCell():
    global x1
    global x2
    for y in range(10,190,25):
        for x in range(110,200,25):
           healthyCell = Cell("healthy", x, y)
           drawhealthyCell = Circle(Point(healthyCell.X, healthyCell.Y), 10)
           drawhealthyCell.draw(win)
           if (x1 >= 55):
               healthyCell.State == "infected"
           if (healthyCell.State == "infected"):
               drawhealthyCell.undraw()
               drawhealthyCell = Circle(Point(healthyCell.X, healthyCell.Y), 10)
               drawhealthyCell.setOutline('red')
               drawhealthyCell.draw(win)

               


def drawPathogen():
    global x1
    global y1
    global pathogen1
    global drawhealthyCell
    
    p = Point(pathogen1.X, pathogen1.Y)
    path = Circle(p, 5)
    path.draw(win)
    path.setFill('red')

    while True:
         a = randrange(-10,10)
         x1 = x1 + a
         b = randrange(-10,10)      
         y1 = y1 + b
         if (x1 > 200):
             x1 = 0
             path.undraw()
             path = Circle(Point(x1,y1), 5)
             path.setFill('red')
             path.draw(win)
         if (x1 < 0):
             x1 = 200
             path.undraw()
             path = Circle(Point(x1,y1), 5)
             path.setFill('red')
             path.draw(win)
         if (y1 > 200):
             y1 = 0
             path.undraw()
             path = Circle(Point(x1,y1), 5)
             path.setFill('red')
             path.draw(win)   
         if (y1 < 0):
             y1 = 200
             path.undraw()
             path = Circle(Point(x1,y1), 5)
             path.setFill('red')
             path.draw(win)
         time.sleep(0.5)
         path.move(a,b)
         printPoint(x1,y1)
         #infectCells()
         


drawCell()
drawPathogen()



