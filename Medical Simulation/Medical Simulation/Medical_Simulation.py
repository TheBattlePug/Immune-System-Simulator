from graphics import *
from random import *
from enum import *
import time

windowHeight = 300
windowWidth = 400

win = GraphWin("Human Body", 1000, 600)


class CellType(Enum):
    T = 1
    B = 2
    HealthyBody = 3
    InfectedBody = 4
    Pathogen = 5
    Dead = 6
    PathogenSpawned = 7
    DeadPathogen = 8
    Macrophage = 9

class Cell:
    def __init__ (self, type, x, y):
        self.Type = type
        self.X = x
        self.Y = y
        self.Visual = 0
        self.Timer = 0
        self.Draw(x, y)
   
    #def Move(self, newX, newY):
    #    if (self.Type != CellType.DeadPathogen):
    #        visual = self.Visual;
    #        visual.undraw()
    #        self.Draw(newX, newY)
    #    else:
    #        self.Visual.undraw()
            
    def Move(self):
        if (self.Type == CellType.B or self.Type == CellType.T or self.Type == CellType.Pathogen or self.Type == CellType.Macrophage):
            speed = 0
            if (self.Type == CellType.B):
                speed = 20
            if (self.Type == CellType.T):
                speed = 40
            if (self.Type == CellType.Pathogen):
                speed = 30
            if (self.Type == CellType.Macrophage):
                speed = 50

            a = randrange( 0 - speed, speed)
            newX = self.X + a
            b = randrange( 0 - speed, speed)      
            newY = self.Y + b

            newX = adjust(newX, windowWidth)
            newY = adjust(newY, windowHeight)

            visual = self.Visual;
            visual.undraw()
            self.Draw(newX, newY)


        if (self.Type == CellType.DeadPathogen):
           self.Visual.undraw()

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
            self.Timer = self.Timer + 1
            if (self.Timer == 50):
                self.Type = CellType.PathogenSpawned
                pathogen1 = Cell(CellType.Pathogen, self.X, self.Y)
                pathogenArray.append(pathogen1)
                pathogen2 = Cell(CellType.Pathogen, self.X, self.Y)
                pathogenArray.append(pathogen2)
          
        if (self.Type == CellType.Macrophage): 
            size = 20
            color = 'orange'
                
        if (self.Type == CellType.Pathogen): 
            size = 5
            color = 'red'

        if (self.Type == CellType.PathogenSpawned):
            size = 10
            color = 'black'

        
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
    
    
        

class Pathogen:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    path = 0

#Creates an array of pathogens that develope over time   
pathogenArray = []
pathogen = Cell(CellType.Pathogen, windowWidth/2, windowHeight/2)
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
tCell = Cell(CellType.T, 10, windowHeight/2)

#bCell parameters
bCell = Cell(CellType.B, windowWidth - 10, windowHeight/2)

#Macrophage parameters
macrophage = Cell(CellType.Macrophage, windowWidth/3, windowHeight/3)
   

def redrawCell():   

    for i in range(0,len(cellArray)):
        cell = cellArray[i]
        
        for j in range(0, len(pathogenArray)):
            pathogen = pathogenArray[j]
            

            # if pathogen touches a healty cell, mark cell as infected and kill mark pathogen as dead.
            if (abs(pathogen.X-cell.X)<=15 and abs(pathogen.Y-cell.Y)<=15 and cell.Type == CellType.HealthyBody):
                cell.Type = CellType.InfectedBody
                pathogen.Type = CellType.DeadPathogen


            # if macrophage touches a pathogen then it kills it.
            if (abs(pathogen.X - macrophage.X) <= 55 and abs(pathogen.Y-macrophage.Y)<= 55):
                pathogen.Type = CellType.DeadPathogen


        # if tCell touches an infected cell, mark as dead.   
        if (abs(tCell.X-cell.X)<=18 and abs(tCell.Y-cell.Y)<=18 and cell.Type == CellType.InfectedBody):
                cell.Type = CellType.Dead

 
           
        cell.Draw(cell.X, cell.Y)
           
def adjust(position, limit):
    ret = position

    if (position > limit):
        ret = limit - 10
             
    if (position < 0):
        ret = 10
            
    return ret  


def ShowLegend():
    plate = Rectangle(Point(0, 0), Point(windowWidth, windowHeight))
    plate.draw(win)

    t1 = Text(Point(windowWidth + 100, 20), "Legend:")
    t1.draw(win)

    h1 = Cell(CellType.HealthyBody,windowWidth + 80, 50 )
    t2 = Text(Point(windowWidth + 150, 50), "Healthy Cells")
    t2.draw(win)

    
    i1 = Cell(CellType.InfectedBody,windowWidth + 80, 80 )
    t3 = Text(Point(windowWidth + 280, 80), "Infected Cells: cells that the pathogen has infected.")
    t4 = Text(Point(windowWidth + 280, 95), "Infected Cells spawn two pathogens after 5 seconds")
    t3.draw(win)
    t4.draw(win)
         

def doAll():
    
    ShowLegend()
    while True:
         for i in range(0, len(pathogenArray)):
             pathogen = pathogenArray[i]
             pathogen.Move()
         
         tCell.Move()
         bCell.Move()
         macrophage.Move()
         redrawCell()
         time.sleep(0.2)
         

doAll()

