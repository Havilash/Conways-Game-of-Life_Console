import time
import numpy
import os
import keyboard

#python Documents\Projects\Programming\Python\ConwaysGameOfLife\ConwaysRules.py

os.system('mode 200,40')
gridBool = numpy.full((200, 39), False)
tempGridBool = numpy.copy(gridBool)
row, column = gridBool.shape
drawerCellPos = [0, 0]
is_running = True

def DrawCell(): 
    global drawerCellPos, key_is_pressed, is_running
    key_is_pressed = False
    while True:
        if keyboard.is_pressed('UP'):
            drawerCellPos[1] -= 1
            key_is_pressed = True
        if keyboard.is_pressed('DOWN'):
            drawerCellPos[1] += 1
            key_is_pressed = True
        if keyboard.is_pressed('LEFT'):
            drawerCellPos[0] -= 1
            key_is_pressed = True
        if keyboard.is_pressed('RIGHT'):
            drawerCellPos[0] += 1
            key_is_pressed = True
        if keyboard.is_pressed('RETURN'):
            return
        if keyboard.is_pressed('D'):
            gridBool[drawerCellPos[0], drawerCellPos[1]] = False
            tempGridBool[drawerCellPos[0], drawerCellPos[1]] = False
            key_is_pressed = True
        if keyboard.is_pressed('F'):
            gridBool[drawerCellPos[0], drawerCellPos[1]] = True
            tempGridBool[drawerCellPos[0], drawerCellPos[1]] = True                
            key_is_pressed = True
        if keyboard.is_pressed('R'):
            for i in range(column):
                for j in range(row):
                    gridBool[i][j] = False
            key_is_pressed = True
        if(key_is_pressed):
            # print(drawerCellPos[0], drawerCellPos[1])
            os.system('cls')
            DrawField()
            key_is_pressed = False
            time.sleep(0.03)

def DrawField():
    global drawerCellPos
    for i in range(column):
        for j in range(row):
            if tempGridBool[j, i]:
                print("#", end= "")
            elif j == drawerCellPos[0] and i == drawerCellPos[1]:
                print("0", end= "")
            else:
                print("-", end= "")
        print()

def CountNeighbours(xPos, yPos):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if xPos + j <= row - 1 and yPos + i <= column - 1 and xPos + j >= 0 and yPos + i >= 0:
                if tempGridBool[xPos + j, yPos + i]:
                    neighbours += 1
    return neighbours

def OverUnderPopulation(xPos, yPos):
    if (CountNeighbours(xPos, yPos) > 4 or CountNeighbours(xPos, yPos) < 3) and tempGridBool[xPos, yPos]:
        gridBool[xPos, yPos] = False

def Alive3Neighbours(xPos, yPos):
    if CountNeighbours(xPos, yPos) == 3 and tempGridBool[xPos, yPos] == False:
        gridBool[xPos, yPos] = True

def Instructions():
    print("Conways Game of Life")
    print("F = Draw Cell")
    print("D = Draw Cell")
    print("R = Reset")
    # print("CTRL + S = Save")
    # print("CTRL + L = Load")
    print("ENTER = Next Generation")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    input("Press Enter to Start")

def StartGame():
    Instructions()
    global tempGridBool, is_running
    DrawField()
    while True:
        if keyboard.is_pressed('RETURN'):
            os.system('cls')
            tempGridBool = numpy.copy(gridBool)
            DrawField()
            for i in range(column):
                for j in range(row):
                    OverUnderPopulation(j, i)
                    Alive3Neighbours(j, i)
            # time.sleep(0.1)
        else:
            DrawCell()

# gridBool[100, 20] = True
# gridBool[99, 19] = True
# gridBool[99, 20] = True
# gridBool[100, 20] = True
# gridBool[100, 21] = True
# gridBool[101, 19] = True
# gridBool[107, 20] = True
# gridBool[108, 20] = True
# gridBool[109, 20] = True
StartGame()