titles = ['DRAWBRIDGE','ROAD','CAVE','WATERFALL','FOREST','CLEARING',
	 'POOL','CABIN IN THE WOODS','CLIFF']
exits = [{'s' : 3, 'e' : 1},
         {'s' : 4, 'e' : 2, 'w' : 0},
         {'s' : 5, 'w' : 1},
         {'n' : 0, 's' : 6, 'e' : 4},
         {'n' : 1, 's' : 7, 'e' : 5, 'w' : 3},
         {'n' : 2, 's' : 8, 'w' : 4},
         {'n' : 3, 'e' : 7},
         {'n' : 4, 'e' : 8, 'w' : 6},
         {'n' : 5, 'w' : 7}]
descriptions = ['You stand at the edge of a moat in front of a drawbridge '
                'in a wall that surrounds a castle to the west. '
                'The drawbridge is currently raised.',
                'You find yourself at the edge of a dusty road that runs '
                'east and west. To the south is a forest.',
                'An east-west road ends abruptly at a cave at the foot '
                'of a large mountain to the east.  To the south, a forest '
                'comes up to the foot of the mountain.  A sign in the cave '
                'entrance says: UNDER CONSTRUCTION.',
                'You stand at the top of a rushing waterfall. '
                'It falls at least 50 feet to a pool that lies to the south. '
                'The river that feeds the falls flows from the north.',
                'You are standing in the middle of a forest. '
                'You hear rushing water to the west. '
                'To the south, you think you might see some smoke through '
                'the trees.',
                'You are standing in a clearing in the middle of the woods. '
                'There is a large oak tree near the center of the clearing.',
                'You are standing at the edge of a pool at the foot '
                'of a waterfall.  You think you see somthing sparkling '
                'below the surface the water. '
                'You see a column of smoke through the trees to the east.',
                'You are standing in front of a log cabin in the middle '
                'of the woods.  Smoke is coming out of its chimney. '
                'The front door is locked, and the curtains are drawn.',
                'You exit the forest and suddenly you find yourself '
                'at the edge of a rocky cliff that drops off steeply to '
                'the south and east. ']
                
direction = ''
currentRoom = 4
quitProgram = False
while True:
    # Show the room's title and decription
    print(" ")
    print(titles[currentRoom])
    print(descriptions[currentRoom])

    while True:
        direction = raw_input("--\nEnter a direction ('q' to quit): ")
        # First check for commands
        if (direction == 'q'):
            quitProgram = True
            break

        # Then see if we have a valid direction 
        elif (direction not in exits[currentRoom]):
            print("You cannot go in that direction.")

        else:
            break

    if quitProgram:
        break
    
    # Move to the new room
    currentRoom=exits[currentRoom][direction]

print("Goodbye!")
raw_input("press Enter to close")

