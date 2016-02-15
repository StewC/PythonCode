#!/usr/bin/python
import math   # This will import math module

## SUDDOKO SOLVER.  Version 1.0
## The solver takes in the starting situation as a list of numbers
## the first number in the list repersents the top left most title
## and then goes from left to right. The solver creates a slolution 
## profile which is a list of lists with the internal lists repersenting
## all possible solutions at that poisiton. The code goes through each 
## position removing numbers that are longer vaild possible solutions
## to reduce the solution space.


# Variables
##Board = [0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0,
##         0,0,0,0,0,0,0,0,0]

Board = [5,0,7,0,0,0,9,0,8,
         0,0,2,0,8,0,0,7,0,
         0,4,0,0,3,7,0,0,5,
         6,1,0,0,7,0,4,0,2,
         7,0,9,0,0,0,5,0,6,
         4,0,5,0,1,0,0,8,3,
         1,0,0,4,2,0,0,5,0,
         0,5,0,0,9,0,1,0,0,
         2,0,4,0,0,0,6,0,9]


SoluProfile = []

## List of the squares that make up the local boxes that must contain
## the values 1-9
Sq1 = [0,1,2,  9,10,11,   18,19,20]
Sq2 = [3,4,5,  12,13,14,  21,22,23]
Sq3 = [6,7,8,  15,16,17,  24,25,26]

Sq4 = [27,28,29, 36,37,38, 45,46,47]
Sq5 = [30,31,32, 39,40,41, 48,49,50]
Sq6 = [33,34,35, 42,43,44, 51,52,53]

Sq7 = [54,55,56, 63,64,65, 72,73,74]
Sq8 = [57,58,59, 66,67,68, 75,76,77]
Sq9 = [60,61,62, 69,70,71, 78,79,80]



def RunSolution(Board):
    # Setup Starting Conditions
    print("---- Starting Conditions ----")

##  Build soulution space
    for i in range(0,81):
        if Board[i] == 0:
            SoluProfile.append([1,2,3,4,5,6,7,8,9])
        else:
            SoluProfile.append([Board[i]])
    LatestBoard = []
    LatestBoard = UpdateBoard(SoluProfile, LatestBoard)
    DisplayCurrentSolutionProfile(SoluProfile)			# Display starting board
    count = 1
    while (count < 10):
        LatestBoard = RefineSoultionProfile(SoluProfile, LatestBoard)		#Solving
        LatestBoard = []
        LatestBoard = UpdateBoard(SoluProfile, LatestBoard)
        count = count + 1
    
    print("---- End Solution Profile ----")
    DisplayCurrentSolutionProfile(SoluProfile)
    print("---- End Answer ----")
    DisplayCurrentBoard(LatestBoard)
    print(" END PROGRAM ")
    return

##  Refine Solution profile based on known Board
def RefineSoultionProfile(SoluProfile, Board):
    for i in range(0,81):
        if len(SoluProfile[i]) > 1:
              CheckHorizontal(i, SoluProfile, Board)
    for i in range(0,81):
        if len(SoluProfile[i]) > 1:
            CheckVertical(i, SoluProfile, Board)
    for i in range(0,81):
            if len(SoluProfile[i]) > 1:
                CheckLocalSquare(i, SoluProfile, Board)
    DisplayCurrentSolutionProfile(SoluProfile)
    for i in range(0,81):
            if len(SoluProfile[i]) > 1:
                CheckIfNumberUnique(i, SoluProfile, Board)
    return Board

def CheckHorizontal(Location, SoluProfile, Board):
    Line = math.floor(Location/9)
    for i in range(0,9):
        TestLocation = (Line * 9) + i
        if TestLocation != Location:
            if Board[TestLocation] in SoluProfile[Location]:
                SoluProfile[Location].remove(Board[TestLocation])
    return

def CheckVertical(Location, SoluProfile, Board):
    Ans = divmod(Location, 9)
    for i in range(0,9):
        TestLocation = (i * 9) + Ans[1]
        if TestLocation != Location:
            if Board[TestLocation] in SoluProfile[Location]:
                SoluProfile[Location].remove(Board[TestLocation])
    return

## Check where there are multiple solutions if one of the solutions
## is the only possible solution
def CheckIfNumberUnique(Location, SoluProfile, Board):
    SoluNum = 0
    # Check if number is unique within soloution profile in the horizontal
    if len(SoluProfile[Location]) > 1:
        for i in range(0,len(SoluProfile[Location])):                     
            TestNum = SoluProfile[Location][i]
            Freq = 0            
            Line = math.floor(Location/9)
            for j in range(0,9):
                TestLocation = (Line * 9) + j
                if TestLocation != Location:
                    if TestNum in SoluProfile[TestLocation]:
                        Freq = Freq + 1
            if Freq == 0: #Not found elsewhere 
                SoluNum = TestNum

    if SoluNum > 0:
        SoluProfile[Location] = [SoluNum]
        SoluNum = 0

    if len(SoluProfile[Location]) > 1:
        for i in range(0,len(SoluProfile[Location])):                      
            TestNum = SoluProfile[Location][i]
            Freq = 0               
            Ans = divmod(Location, 9)
            for j in range(0,9):
                TestLocation = (j * 9) + Ans[1]
                if TestLocation != Location:
                    if TestNum in SoluProfile[TestLocation]:
                        Freq = Freq + 1  
            if Freq == 0: #Not found elsewhere
                SoluNum = TestNum
    if SoluNum > 0:
        SoluProfile[Location] = [SoluNum]
        SoluNum = 0

    if len(SoluProfile[Location]) > 1:
        for i in range(0,len(SoluProfile[Location])):
            # Check Sq
            Freq = 0
            Sq= []
            Sq = LocalSqaureIS(Location)
            for j in range(0,9):
                TestLocation = Sq[j]
                if TestLocation != Location:
                    if TestNum in SoluProfile[TestLocation]:
                        Freq = Freq + 1
            if Freq == 0: #Not found elsewhere
                SoluNum = TestNum
    if SoluNum > 0:
        SoluProfile[Location] = [SoluNum]
        SoluNum = 0

    return



def CheckLocalSquare(Location, SoluProfile, Board):
    Sq= []
    Sq = LocalSqaureIS(Location)
    for i in range(0,9):
        TestLocation = Sq[i]
        if TestLocation != Location:
            if Board[TestLocation] in SoluProfile[Location]:
                SoluProfile[Location].remove(Board[TestLocation])

    return

def LocalSqaureIS(Location):
    if Location in Sq1:
        return Sq1
    if Location in Sq2:
        return Sq2
    if Location in Sq3:
        return Sq3
    if Location in Sq4:
        return Sq4
    if Location in Sq5:
        return Sq5
    if Location in Sq6:
        return Sq6
    if Location in Sq7:
        return Sq7
    if Location in Sq8:
        return Sq8
    if Location in Sq9:
        return Sq9


def UpdateBoard(SoluProfile, LatestBoard):
    for i in range(0,81):
        if len(SoluProfile[i]) == 1:
            l = SoluProfile[i]
            LatestBoard.append(l[0])
        else:
            LatestBoard.append(0)
    return LatestBoard

def DisplayCurrentSolutionProfile(SoluProfile):
    print("*******************")
    print(str(SoluProfile[0:9]))
    print(str(SoluProfile[9:18]))
    print(str(SoluProfile[18:27]))
    print(str(SoluProfile[27:36]))
    print(str(SoluProfile[36:45]))
    print(str(SoluProfile[45:54]))
    print(str(SoluProfile[54:63]))
    print(str(SoluProfile[63:72]))
    print(str(SoluProfile[72:81]))

    print("*******************")
    return

def DisplayCurrentBoard(Board):
    DisplayCurrentSolutionProfile(Board)
    return
    

RunSolution(Board)

print("End")
