def generateGrid(path):
    grid = []
    with open(path, 'r') as f:
        line = f.readline().replace('\n', '')
        while line:
            l = list(map(int, list(line)))
            grid.append(l)
            line = f.readline().replace('\n', '')
    return grid

def findLowPoints(grid):
    lowPoints = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check neighbors
            # North
            if i > 0 and grid[i-1][j] <= grid[i][j]:
                continue
            # East
            if j > 0 and grid[i][j-1] <= grid[i][j]:
                continue
            # South
            if i < len(grid)-1 and grid[i+1][j] <= grid[i][j]:
                continue
            # West
            if j < len(grid[i])-1 and grid[i][j+1] <= grid[i][j]:
                continue
            lowPoints[(i, j)] = grid[i][j]
    return lowPoints

def calcRisk(lowPoints):
    return sum(lowPoints.values()) + len(lowPoints)

def findBasins(grid, lowPoints):
    basins = {}
    for coord in lowPoints:
        basin = [coord]
        coordsToCheck = [coord]
        coordsChecked = {}
        coordsChecked[coord] = True
        while coordsToCheck:
            c = coordsToCheck.pop(0)
            i = c[0]
            j = c[1]
            # North
            north = (i-1,j)
            if i > 0 and north not in coordsChecked and grid[i-1][j] != 9:
                basin.append(north)
                coordsToCheck.append(north)
                coordsChecked[north] = True
            # East
            east = (i,j-1)
            if j > 0 and east not in coordsChecked and grid[i][j-1] != 9:
                basin.append(east)
                coordsToCheck.append(east)
                coordsChecked[east] = True
            # South
            south = (i+1,j)
            if i < len(grid)-1 and south not in coordsChecked and grid[i+1][j] != 9:
                basin.append(south)
                coordsToCheck.append(south)
                coordsChecked[south] = True
            # West
            west = (i,j+1)
            if j < len(grid[i])-1 and west not in coordsChecked and grid[i][j+1] != 9:
                basin.append(west)
                coordsToCheck.append(west)
                coordsChecked[west] = True
        basins[coord] = basin
    return basins

def part1(path):
    grid = generateGrid(path)
    lowPoints = findLowPoints(grid)
    return calcRisk(lowPoints)

def part2(path):
    grid = generateGrid(path)
    lowPoints = findLowPoints(grid)
    basins = findBasins(grid, lowPoints)
    sortedBasins = list(basins.values())
    sortedBasins.sort(key=lambda x: len(x))
    return len(sortedBasins[-1]) * len(sortedBasins[-2]) * len(sortedBasins[-3])

if __name__ == '__main__':
    path = 'Day9/input.txt'
    # Part 1: 456
    print(part1(path))
    # Part 2: 1047744
    print(part2(path))