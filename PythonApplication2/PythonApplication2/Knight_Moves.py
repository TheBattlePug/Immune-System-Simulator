#This program is designed to repeat an algorithem

class Point:
    def __init__(self, x, y):  
        self.X = x  
        self.Y = y  

def printPoint(point:Point):
    print("[", str(point.X), ",", str(point.Y), "]")

def jump(point:Point, stepCount:int):

    if(stepCount >= 4):
        #print ("Reached max number of moves. Exit path")
        return 0

    if(point.X == 6 and point.Y == 1):
        print ("Reached Destination in ", str(stepCount), " steps. Success")
        printPoint(point)
        return 1

    pointList = moveList(point)
    for p in pointList:
        ret = jump(p, stepCount+1)
        if (ret == 1):
            print("Step ", stepCount)
            printPoint(point)
            return 1

    return 0



def moveList(fromCoordinates:Point):

    possibleMoves = []
    
    newMove = Point(fromCoordinates.X+1, fromCoordinates.Y+2 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X+1, fromCoordinates.Y-2 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X-1, fromCoordinates.Y+2 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X-1, fromCoordinates.Y-2 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X+2, fromCoordinates.Y+1 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X+2, fromCoordinates.Y-1 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X-2, fromCoordinates.Y+1 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    newMove = Point(fromCoordinates.X-2, fromCoordinates.Y-1 )
    if (newMove.X <= 7 and newMove.X >= 0 and newMove.Y <= 7 and newMove.Y >= 0):
        possibleMoves.append(newMove)

    
    return(possibleMoves)
       

def main():
    start = Point(0,0)
    ret = jump(start,0)
    if (ret == 0):
        print ("No Path Found")