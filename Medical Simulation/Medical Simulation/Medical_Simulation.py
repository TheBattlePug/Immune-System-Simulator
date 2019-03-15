from graphics import *
from random import *
from enum import *
import time

windowHeight = 300
windowWidth = 400

win = GraphWin("Human Body", windowWidth, windowHeight)

class CellType(Enum):
    T = 1
    B = 2
    HealthyBody = 3
    InfectedBody = 4
    Pathogen = 5
    Dead = 6
    

class Cell:
    def __init__ (self, type, x, y):
        self.Type = type
        self.X = x
        self.Y = y
        self.Visual = 0

        self.Draw(x, y)
   
    def Move(self, newX, newY):
        
        visual = self.Visual;
        visual.undraw()
        self.Draw(newX, newY)
        

    def Draw(self, x, y):
        
        size = 1
        color = 'black'

        if (self.Type == CellType.Dead):
            size = 10
            color = 'gray'

        if (self.Type == CellType.T):
            size = 8
            color = 'blue'

        if (self.Type == CellType.B): 
            size = 15
            color = 'yellow'
       
        if (self.Type == CellType.HealthyBody): 
            size = 10
            color = 'black'

        if (self.Type == CellType.InfectedBody): 
            size = 10
            color = 'red'

        if (self.Type == CellType.Pathogen): 
            size = 5
            color = 'red'
        

        p = Point(x, y)
        visual = Circle(p, size)

        if (self.Type == CellType.HealthyBody or self.Type == CellType.InfectedBody):
            visual.setOutline(color)
        else: 
            visual.setFill(color)

        visual.draw(win)
        self.Visual = visual
        self.X = x
        self.Y = y
    
    def Kill(self):
        self.Type = CellType.Dead

class Pathogen:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    path = 0

def printPoint(x, y):
    print("(", x, ",", y, ")")

#Creates an array of pathogens that develope over time   
pathogenArray = []
pathogen = Cell(CellType.Pathogen, 50, 100)
pathogenArray.append(pathogen)

# Creates an array of a cells
cellAmount = 25
cellArray = []

for i in range(0, cellAmount):
    h = randrange(20, windowHeight-20)
    w = randrange(20, windowWidth-20)
    s = Cell(CellType.HealthyBody, w, h)
    cellArray.append(s)

#tCell parameters
tCell = Cell(CellType.T, -10, windowHeight/2)


   

def redrawCell():
    
    x1 = pathogenArray[0].X
    y1 = pathogenArray[0].Y

    

    for i in range(0,len(cellArray)):
        cell = cellArray[i]
        
        # if patogen touches a healty cell, mark cell as infected
        if (abs(x1-cell.X)<=15 and abs(y1-cell.Y)<=15 and cell.Type == CellType.HealthyBody):
            cell.Type = CellType.InfectedBody
               
        # if tCell touches an infected cell, mark as dead.   
        if (abs(tCell.X-cell.X)<=18 and abs(tCell.Y-cell.Y)<=18 and cell.Type == CellType.InfectedBody):
                cell.Kill()
           
        cell.Draw(cell.X, cell.Y)
           
def adjust(position, limit):
    ret = position

    if (position > limit):
        ret = limit - 10
             
    if (position < 0):
        ret = 10
            
    return ret  
              
              

    
              
def movePathogen():
    
    for i in range(0, len(pathogenArray)):
        pathogen = pathogenArray[i]
 
        a = randrange(-20,20)
        newX = pathogen.X + a
        b = randrange(-20,20)      
        newY = pathogen.Y + b

        newX = adjust(newX, windowWidth)
        newY = adjust(newY, windowHeight)
        pathogen.Move(newX, newY)

def movetCell():
    
        a = randrange(-40,40)
        newX = tCell.X + a
        b = randrange(-40,40)      
        newY = tCell.Y + b

        newX = adjust(newX, windowWidth)
        newY = adjust(newY, windowHeight)

        tCell.Move(newX, newY)



def doAll():
    

    while True:
         movePathogen()
         movetCell()
         redrawCell()
         time.sleep(0.2)
         

doAll()

