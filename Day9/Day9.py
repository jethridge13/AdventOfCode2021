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

def part1(path):
    grid = generateGrid(path)
    lowPoints = findLowPoints(grid)
    return calcRisk(lowPoints)

def part2(path):
    pass

if __name__ == '__main__':
    path = 'Day9/input.txt'
    # Part 1: 456
    print(part1(path))
    # Part 2: 
    print(part2(path))