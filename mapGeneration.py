# mapGeneration: World Generation for transversal, with start and goal points
# Assignment 1 - A* and heurist functions
# CS 4341 - Intro to AI
# Written by: Lucas Ruiz Lebrao

import random

def saveMap( map, filename):
    # Get filename
    #filename = raw_input("Provide a filename: ");
    
    # Open a new file
    fo = open(filename + ".txt", "w");

    # Save list into file
    for i in range(len(map)):
        for j in range(len(map[0])):
            fo.write("%s" %(Map[i][j]))
            if j is not len(map[0]) - 1:
                fo.write("\t")
        fo.write("\n");

#Declare variables
over = 0
action = 0

#while over == 0:
    
# 1: Declaring Variables
columns = input("Enter a number of columns: ");
rows = input("Enter a number of rows: ");
numMaps = input("Enter number of maps to generate: ")
filename = raw_input("Provide a filename: ");
generatedMaps = 0

while generatedMaps is not numMaps:
    # Creates a list containing 2 lists initialized to 0
    Map = [[0 for x in range(columns)] for x in range(rows)]

    # 2: Determine Start and Goal
    start = (random.randint(0, rows-1), random.randint(0, columns-1))
    goal = start
    while start == goal:
        goal = (random.randint(0, rows-1), random.randint(0, columns-1))

    print
    print "Start Point = ", start
    print "End Point = ", goal

    # 3: Fill Map 
    for i in range(rows):
        for j in range(columns):
            if ((i,j) == start):
                Map[i][j] = 'S';
            elif ((i,j) == goal):
                Map[i][j] = 'G';
            else:
                Map [i][j] = random.randint(1, 9)
            print "%s\t" % Map[i][j],
        print

    saveMap(Map, filename + str(generatedMaps))
    generatedMaps += 1
"""
    # 4: Determine user action
    action = 0
    while action == 0 :
        decision = raw_input("\nChoose:\n n - Discard and Generate New Map\n c - Save and Continue\n s - Save and Quit\n q - Quit\n >> ");

        if decision == 'n':   # New
            action = 1
        elif decision == 'c': # Save/Cont
            saveMap(Map)
            action = 1
        elif decision == 's': # Save/Quit
            saveMap(Map)
            action = 1
            over = 1
        elif decision == 'q': # Quit
            action = 1
            over = 1
        else:
            print ("Not a Valid Input!");
    
"""