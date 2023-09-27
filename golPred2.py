import copy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

start = 20 # how many cells start on
side = 10   # how many cells should there be?

state = [] # set up an empty list to fill
reports = []

#Randomize starting locations
births = []
for i in range(start):
    check = random.randint(0, side*side)
    while check in births:
        check = random.randint(0, side*side)
    births.append(check)

#Initialize the board
for i in range(side):
    row = []
    for j in range(side):
        row.append(0)
        if i*side + j in births:
            row[-1]=1
    state.append(row)

#Initialize Plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7), height_ratios=[3, 1])
ax1.imshow(state, cmap=mpl.colormaps['cividis'])
ax1.set_xlabel('X Position')
ax1.set_ylabel('Y Position')
ax2.plot(range(len(reports)), reports)
ax2.set_xlabel('Step of Simulation')
ax2.set_ylabel('Number of Living Cells')
plt.ion()
plt.show(block=False)
plt.pause(1)


def drawPred(y, x, cur):
    newState=copy.deepcopy(cur)
    newState[y][x] = 2
    newState[y][x+1] = 2
    newState[y][x-1] = 2
    newState[y+1][x-1] = 2
    newState[y-1][x+1] = 2
    newState[y+1][x+1] = 2
    newState[y+1][x] = 2
    newState[y-1][x] = 2
    newState[y-1][x-1] = 2
   
   
    del cur
    return newState
   
   
startY = 5
startX = 5
   
#Creating a function
def animate(cur):
    newState=copy.deepcopy(cur)#Needed so that newState cannot affect old state (cur)
    for i in range(side):
        for j in range(side):
            numAlive = 0
            #Determine the number of adjacent squares currently 'alive'
            for k in range(3):
                for L in range(3):
                    try:
                        numAlive += cur[i+k-1][j+L-1]
                        #print(5*i + j, i+k-1, j+L-1, cur[i+k-1][j+L-1])
                    except:
                        IndexError
            numAlive = numAlive - cur[i][j]
            if cur[i][j] == 1:
                if numAlive < 2 or numAlive > 3:
                    newState[i][j] = 0
            if cur[i][j] == 0:
                if numAlive == 3:
                    newState[i][j] = 1
            if cur[i][j] == 0:
                newState = drawPred(startY, startX, newState)
               
            #if cur [i][j]==0:
               # if numAlive < 1:
                    #newState[i][j] = 2
    # for num in range(len(newState)):
    #     print(newState[num], cur[num])
    del cur
    return newState

#Run the simulation
for i in range(100):
    #Update the system state
    state = animate(state)
    living = [x for line in state for x in line if x > 0]
    reports.append(len(living))
    ax1.imshow(state, cmap=mpl.colormaps['cividis'])
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')
    ax2.cla()
    ax2.plot(range(len(reports)), reports)
    ax2.set_xlabel('Step of Simulation')
    ax2.set_ylabel('Number of Living Cells')
    plt.draw()
    plt.show(block=False)
    plt.pause(0.1)
    if not len(living) > 0:
        break

plt.show(block=False)
input('Press "Enter" to quit')
