from graphics import *
from random import randrange
import time


win = GraphWin()
x = 100
y = 100
circ = Circle(Point(x,y), 10)

def move():
    global x
    global y
    global circ
    print("How you move object:")
    print("'right' means to move 10 units right.")
    print("'left' means to move 10 units left.")
    print("'up' means to move 10 units up.")
    print("'down' means to move 10 units down.")
    print("")

    move = input("which way do I move: ")

    if move == "left":
        x = x - 10
        circ.move(-10,0)
        print(x)
        print(y)
    if move == "right":
        x = x + 10
        circ.move(10,0)
        print(x)
        print(y)
    if move == "up":
        y = y - 10
        circ.move(0,-10)
        print(x)
        print(y)
    if move == "down":
        circ.move(0,10)
        y = y + 10
        print(x)
        print(y)

        
        
        

        
        
def drawObject(x, y):
     circ.draw(win)
     circ.setFill('black')    

def randomCircle():
     r1 = Line(Point(0,100), Point(200,100))
     r2 = Line(Point(100,0), Point(100,200))
     l1 = Text(Point(50,50), "x < 100,")
     l2 = Text(Point(50,150), "x < 100," )
     l3 = Text(Point(150,50), "x > 100,")
     l4 = Text(Point(150,150), "x > 100,")
     l5 = Text(Point(50,70), "y > 100")
     l6 = Text(Point(50, 170), "y > 100")
     l7 = Text(Point(150, 70), "y < 100")
     l8 = Text(Point(150, 170), "y > 100")
     a = randrange(0,200)
     b = randrange(0,200)
     p = Circle(Point(a,b), 10)
     print("(", a, ",", b, ")")
     p.draw(win)
     r1.draw(win)
     r2.draw(win)
     l1.draw(win)
     l2.draw(win)
     l3.draw(win)
     l4.draw(win)
     l5.draw(win)
     l6.draw(win)
     l7.draw(win)
     l8.draw(win)
     #this is where the circle changes position
     while True:
         c = randrange(-50,50)
         time.sleep(3)
         print(a)
         a = a + c
         time.sleep(1)
         print("change:", c)
         d = randrange(-50,50)
         time.sleep(1)
         print(b)
         b = b + d
         time.sleep(1)
         print("change:", d)
         if (a > 200):
             a = 0
             p.undraw()
             p = Circle(Point(a,b), 10)
             p.draw(win)
         if (a < 0):
             a = 200
             p.undraw()
             p = Circle(Point(a,b), 10)
             p.draw(win)
         if (b > 200):
             b = 0
             p.undraw()
             p = Circle(Point(a,b), 10)
             p.draw(win)   
         if (b < 0):
             b = 200
             p.undraw()
             p = Circle(Point(a,b), 10)
             p.draw(win)
         time.sleep(1)
         p.move(c,d)
         print("(", a, ",", b, ")")
         
randomCircle()          
        
          
