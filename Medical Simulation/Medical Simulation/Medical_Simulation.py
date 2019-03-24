from graphics import *
from random import *
from enum import *
import time
from math import *

windowHeight = 300
windowWidth = 500

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
        self.MovementAngle = 0
        self.MovingSpeed = 0
        self.Size = 10


        if (self.Type == CellType.B):
            self.MovingSpeed = 10 
            self.MovementAngle = randrange(0,360)
            self.Size = 15

        if (self.Type == CellType.T):
            self.MovingSpeed = 20
            self.MovementAngle = randrange(0,360)
            self.Size = 8

        if (self.Type == CellType.Pathogen):
            self.MovingSpeed = 15
            self.MovementAngle = randrange(0,360)
            self.Size = 5

        if (self.Type == CellType.Macrophage):
            self.MovingSpeed = 20
            self.MovementAngle = randrange(0,360)
            self.Size = 20

        if (self.Type == CellType.DeadPathogen):
            self.MovingSpeed = 0
            self.Size = 5

        self.Draw(x, y)
   
    
    def Move(self):
        if (self.MovingSpeed > 0):

            a = self.MovingSpeed * cos(self.MovementAngle)
            newX = self.X + a
            b = self.MovingSpeed * sin(self.MovementAngle)
            newY = self.Y + b

         
            if (newX > windowWidth - self.Size or newX < self.Size):
                self.MovementAngle = 180 - self.MovementAngle

            if (newY > windowHeight - self.Size or newY < self.Size):
                self.MovementAngle = 360 - self.MovementAngle





            visual = self.Visual;
            visual.undraw()
            self.Draw(newX, newY)


        if (self.Type == CellType.DeadPathogen):
           self.Visual.undraw()

    def Draw(self, x, y):
        
        size = 1
        color = 'black'
        
        if (self.Type == CellType.Dead):
            color = 'gray'

        if (self.Type == CellType.T):
            color = 'blue'

        if (self.Type == CellType.B): 
            color = 'yellow'
        
        if (self.Type == CellType.HealthyBody): 
            color = 'black'

        if (self.Type == CellType.InfectedBody): 
            color = 'red'
            self.Timer = self.Timer + 1
            if (self.Timer == 50):
                self.Type = CellType.PathogenSpawned
                pathogen1 = Cell(CellType.Pathogen, self.X, self.Y)
                pathogenArray.append(pathogen1)
                pathogen2 = Cell(CellType.Pathogen, self.X, self.Y)
                pathogenArray.append(pathogen2)
          
        if (self.Type == CellType.Macrophage): 
            color = 'orange'
                
        if (self.Type == CellType.Pathogen):
            color = 'red'

        if (self.Type == CellType.PathogenSpawned):
            color = 'black'

        
        p = Point(x, y)
        visual = Circle(p, self.Size)

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
           



def ShowLegend():
    plate = Rectangle(Point(0, 0), Point(windowWidth, windowHeight))
    plate.draw(win)

    t1 = Text(Point(windowWidth + 100, 20), "Legend:")
    t1.draw(win)

    h1 = Cell(CellType.HealthyBody, windowWidth + 80, 50 )
    t2 = Text(Point(windowWidth + 150, 50), "Healthy Cells")
    t2.draw(win)

    h2 = Cell(CellType.InfectedBody, windowWidth + 80, 80 )
    t3 = Text(Point(windowWidth + 280, 80), "Infected Cells: cells that the pathogen has infected.")
    t4 = Text(Point(windowWidth + 287, 95), "Infected Cells spawn two pathogens after 5 seconds.")
    t3.draw(win)
    t4.draw(win)

    h5 = Cell(CellType.Dead, windowWidth + 80, 125)
    t8 = Text(Point(windowWidth + 276, 125), "Killed Cells: infected cells that were killed by T-Cell" )
    t8.draw(win)

    h3 = Cell(CellType.PathogenSpawned, windowWidth + 80, 155)   
    t5 = Text(Point(windowWidth + 277, 155), "Dead Cells: cells that have been infected, but they")
    t6 = Text(Point(windowWidth + 225, 170), "have now released two pathogens.")
    t5.draw(win)
    t6.draw(win)

    h4 = Cell(CellType.Pathogen, windowWidth + 80, 210)
    t7 = Text(Point(windowWidth + 259, 210), "Pathogen: a virus that infects cells to multiply.")
    t7.draw(win)

    h6 = Cell(CellType.Macrophage, windowWidth + 80, 240)
    t9 = Text(Point(windowWidth + 288, 235), "Macrophage: immune cell that engulfs pathogen and")
    t10 = Text(Point(windowWidth + 129, 250), "kills it.")
    t9.draw(win)
    t10.draw(win)


    h7 = Cell(CellType.B, windowWidth + 80, 280)
    t11 = Text(Point(windowWidth + 290, 280), "B-Cell: Releases antibodies that traps the pathogen")
    t12 = Text(Point(windowWidth + 205, 295), "and restricts its movement.")
    t11.draw(win)
    t12.draw(win)

    h8 = Cell(CellType.T, windowWidth + 80, 325)
    t13 = Text(Point(windowWidth + 198, 325), "T-Cell: kills infected cells")
    t13.draw(win)




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

