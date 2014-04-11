rooms = ['DRAWBRIDGE','ROOM 1','ROOM 2','WATERFALL','FOREST','CLEARING',
	 'POOL','CABIN IN THE WOODS','CLIFF']
exits = [{'s' : 3, 'e' : 1},
         {'s' : 4, 'e' : 2, 'w' : 0},
         {'s' : 5, 'w' : 1},
         {'n' : 0, 's' : 6, 'e' : 4},
         {'n' : 1, 's' : 7, 'e' : 3, 'w' : 5},
         {'n' : 2, 's' : 8, 'w' : 4},
         {'n' : 3, 'e' : 7},
         {'n' : 4, 'e' : 8, 'w' : 6},
         {'n' : 5, 'w' : 7}]
direction = ''
currentRoom = 5
while (direction != 'q'):
    print(rooms[currentRoom])
    direction = input("Enter a direction ('q' to quit): ")
    if (direction not in exits[currentRoom]):
        print("You cannot go in that direction.")
    else:
        currentRoom=exits[currentRoom][direction]


