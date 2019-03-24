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
            self.Size = 15

        if (self.Type == CellType.DeadPathogen):
            self.MovingSpeed = 0
            self.Size = 5

        self.Draw(x, y)
   
    
    def Move(self):
        if (self.MovingSpeed > 0):

            a = self.MovingSpeed * cos(radians(self.MovementAngle))
            newX = self.X + a
            b = self.MovingSpeed * sin(radians(self.MovementAngle))
            newY = self.Y + b

         
            if (newX > windowWidth - self.Size or newX < self.Size):
                self.MovementAngle = 180 - self.MovementAngle
                newX = self.X

            if (newY > windowHeight - self.Size or newY < self.Size):
                self.MovementAngle = 360 - self.MovementAngle
                newY = self.Y




            visual = self.Visual;
            visual.undraw()
            self.Draw(newX, newY)


        if (self.Type == CellType.DeadPathogen):
           self.Visual.undraw()
           self.MovingSpeed = 0

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
        del self.Visual
        self.Visual = visual
        self.X = x
        self.Y = y
    
    
        


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
#bCell = Cell(CellType.B, windowWidth - 10, windowHeight/2)

#Macrophage parameters
macrophageAmount = 2
macrophageArray = []
for i in range(0, macrophageAmount):
    h = randrange(20, windowHeight-20)
    w = randrange(20, windowWidth-20)
    s = Cell(CellType.Macrophage, w, h)
    macrophageArray.append(s)


   

def redrawCell():   

    for cell in cellArray:
        
        
        for pathogen in pathogenArray:
            

            # if pathogen touches a healty cell, mark cell as infected and kill mark pathogen as dead.
            if (abs(pathogen.X-cell.X) <= (cell.Size + pathogen.Size) and abs(pathogen.Y-cell.Y) <= (cell.Size + pathogen.Size) and cell.Type == CellType.HealthyBody):
                cell.Type = CellType.InfectedBody
                pathogen.Type = CellType.DeadPathogen


            # if macrophage touches a pathogen then it kills it.
            for m in macrophageArray: 
                if (abs(pathogen.X - m.X) <= (m.Size + pathogen.Size) and abs(pathogen.Y-m.Y) <= (m.Size + pathogen.Size)):
                    pathogen.Type = CellType.DeadPathogen


        # if tCell touches an infected cell, mark as dead.   
        if (abs(tCell.X-cell.X) <= (tCell.Size + cell.Size) and abs(tCell.Y-cell.Y) <= (tCell.Size + cell.Size) and cell.Type == CellType.InfectedBody):
                cell.Type = CellType.Dead

 
          
        cell.Draw(cell.X, cell.Y)
           



def ShowLegend():
    plate = Rectangle(Point(0, 0), Point(windowWidth, windowHeight))
    plate.draw(win)

    rowY = 20

    t1 = Text(Point(windowWidth + 100, rowY), "Legend:")
    t1.draw(win)
    
    rowY += 30

    h4 = Cell(CellType.Pathogen, windowWidth + 80, rowY)
    t7 = Text(Point(windowWidth + 216, rowY), "Virus: infects cells and multiplies.")
    t7.draw(win)
    
    rowY += 30

    h8 = Cell(CellType.T, windowWidth + 80, rowY)
    t13 = Text(Point(windowWidth + 189, rowY), "T-Cell: kills infected cells.")
    t13.draw(win)

    rowY += 30

    h1 = Cell(CellType.HealthyBody, windowWidth + 80, rowY )
    t2 = Text(Point(windowWidth + 150, rowY), "Healthy Cells")
    t2.draw(win)

    rowY += 30

    h2 = Cell(CellType.InfectedBody, windowWidth + 80, rowY )
    t3 = Text(Point(windowWidth + 259, rowY), "Infected Cells: cells that the virus has infected.")

    rowY += 18

    t4 = Text(Point(windowWidth + 270, rowY), "Infected Cells spawn two viruses after 5 seconds.")
    t3.draw(win)
    t4.draw(win)

    rowY += 30

    h5 = Cell(CellType.Dead, windowWidth + 80, rowY)
    t8 = Text(Point(windowWidth + 276, rowY), "Killed Cells: infected cells that were killed by T-Cell." )
    t8.draw(win)

    rowY += 30

    h3 = Cell(CellType.PathogenSpawned, windowWidth + 80, rowY)   
    t5 = Text(Point(windowWidth + 257, rowY), "Dead Cells: cells that have been infected and")

    rowY += 18

    t6 = Text(Point(windowWidth + 194, rowY), "have released two viruses.")
    t5.draw(win)
    t6.draw(win)

    rowY += 30
   

    h6 = Cell(CellType.Macrophage, windowWidth + 80, rowY)
    t9 = Text(Point(windowWidth + 253, rowY), "Macrophage: immune cell that kills viruses.")
    t9.draw(win)
    rowY += 30

    #h7 = Cell(CellType.B, windowWidth + 80, 280)
    #t11 = Text(Point(windowWidth + 290, 280), "B-Cell: Releases antibodies that traps the pathogen")
    #t12 = Text(Point(windowWidth + 205, 295), "and restricts its movement.")
    #t11.draw(win)
    #t12.draw(win)

    




def doAll():
    
    ShowLegend()
    while True:
         
         for pathogen in pathogenArray:
             pathogen.Move()
         

         tCell.Move()

         for m in macrophageArray:
            m.Move()

         redrawCell()
         time.sleep(0.2)

         activePathogens = False
         for p in pathogenArray:
             if (p.Type == CellType.Pathogen):
                 activePathogens = True
         
         infectedCells = False
         for c in cellArray:
             if (c.Type == CellType.InfectedBody):
                 infectedCells = True
       


         if (not activePathogens and not infectedCells):
            print("All pathogens have been killed.")
            print("The immune system has won")
            break

         healthyCells = False
         for c in cellArray:
             if (c.Type == CellType.HealthyBody):
                 healthyCells = True

         if (not healthyCells):

            print("There are no more healthy cells")
            print("The pathogens have won")
            break


doAll()

