def createGrid(path):
    grid = []
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n', '')
            row = list(map(int, list(line)))
            grid.append(row)
            line = f.readline()
    return grid

def simulate(grid):
    count = 0
    flashCoords = []
    flashed = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                flashed[(i,j)] = True
                flashCoords.append((i,j))
    while flashCoords:
        coord = flashCoords.pop(0)
        i, j = coord[0], coord[1]
        grid[i][j] = 0
        flashed[coord] = True
        count += 1
        # North
        north = (i-1,j)
        if i > 0 and north not in flashed:
            grid[i-1][j] += 1
            if grid[i-1][j] > 9:
                flashCoords.append(north)
                flashed[north] = True
        # Northeast
        northeast = (i-1,j+1)
        if i > 0 and j < len(grid[i])-1 and northeast not in flashed:
            grid[i-1][j+1] += 1
            if grid[i-1][j+1] > 9:
                flashCoords.append(northeast)
                flashed[northeast] = True
        # East
        east = (i,j+1)
        if j < len(grid[i])-1 and east not in flashed:
            grid[i][j+1] += 1
            if grid[i][j+1] > 9:
                flashCoords.append(east)
                flashed[east] = True
        # Southeast
        southeast = (i+1,j+1)
        if i < len(grid)-1 and j < len(grid[i])-1 and southeast not in flashed:
            grid[i+1][j+1] += 1
            if grid[i+1][j+1] > 9:
                flashCoords.append(southeast)
                flashed[southeast] = True
        # South
        south = (i+1,j)
        if i < len(grid)-1 and south not in flashed:
            grid[i+1][j] += 1
            if grid[i+1][j] > 9:
                flashCoords.append(south)
                flashed[south] = True
        # Southwest
        southwest = (i+1,j-1)
        if i < len(grid)-1 and j > 0 and southwest not in flashed:
            grid[i+1][j-1] += 1
            if grid[i+1][j-1] > 9:
                flashCoords.append(southwest)
                flashed[southwest] = True
        # West
        west = (i,j-1)
        if j > 0 and west not in flashed:
            grid[i][j-1] += 1
            if grid[i][j-1] > 9:
                flashCoords.append(west)
                flashed[west] = True
        # Northwest
        northwest = (i-1,j-1)
        if i > 0 and j > 0 and northwest not in flashed:
            grid[i-1][j-1] += 1
            if grid[i-1][j-1] > 9:
                flashCoords.append(northwest)
                flashed[northwest] = True
    return count

def getFirstSyncFlash(grid):
    turn = 0
    gridSize = 0
    for i in grid:
        gridSize += len(i)
    while True:
        turn += 1
        count = simulate(grid)
        if count == gridSize:
            return turn

def part1(path):
    grid = createGrid(path)
    count = 0
    for i in range(100):
        count += simulate(grid)
    return count

def part2(path):
    grid = createGrid(path)
    return getFirstSyncFlash(grid)

if __name__ == '__main__':
    path = 'Day11/input.txt'
    # Part 1: 1655
    print(part1(path))
    # Part 2: 337
    print(part2(path))