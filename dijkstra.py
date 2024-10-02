def path_finder(area):
    maze = []
    mazeLayer = []
    
    for line in area.splitlines():
        maze.append([int(char) for char in line])
        
    dimensions = len(maze)

    djk = {(0, 0): [[False, True, True, False], 0]}
    oldX, oldY = 0, 0
    
    while djk:
        if (oldX, oldY) in djk:
            directions, currentWeight = djk.pop((oldX, oldY))
        else:
            break
        
        if (oldX, oldY) == (dimensions - 1, dimensions - 1):
            return currentWeight
        
        for direction in range(4):
            if directions[direction]:
                #North
                if direction == 0:
                    x, y = oldX, oldY - 1
                #East
                elif direction == 1:
                    x, y = oldX + 1, oldY
                #South
                elif direction == 2:
                    x, y = oldX, oldY + 1
                #Wheat
                else:
                    x, y = oldX - 1, oldY
                
                if 0 <= x < dimensions and 0 <= y < dimensions:
                    new_weight = abs(maze[y][x] - maze[oldY][oldX]) + currentWeight
                    
                    if (x, y) in djk:
                        if new_weight < djk[(x, y)][1]:
                            djk[(x, y)][1] = new_weight
                    else:
                        djk[(x, y)] = [[True, True, True, True], new_weight]
                    
                    djk[(x, y)][0][(direction + 2) % 4] = False
        
        minimum = float('inf')
        for coords in djk:
            if djk[coords][1] < minimum:
                minimum = djk[coords][1]
                oldX, oldY = coords
    
    return None

print(path_finder("\n".join([
    "010",
    "010",
    "010"
])))
