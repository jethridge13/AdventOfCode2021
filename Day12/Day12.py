class Cave:

    def __init__(self, letter):
        self.name = letter
        self.isBig = not letter.lower() == self.name
        self.connections = []
        self.terminal = letter == 'start' or letter == 'end'

def buildCaveMap(path):
    caveMap = {}
    with open(path, 'r') as f:
        line = f.readline().replace('\n', '')
        while line:
            caves = line.split('-')
            if caves[0] not in caveMap:
                caveMap[caves[0]] = Cave(caves[0])
            if caves[1] not in caveMap:
                caveMap[caves[1]] = Cave(caves[1])
            caveMap[caves[0]].connections.append(caves[1])
            caveMap[caves[1]].connections.append(caves[0])
            line = f.readline().replace('\n', '')
    return caveMap

def findAllPaths(caveMap):
    return findAllPathsHelper(caveMap, 'start', ['start'], [], {'start': True})

def findAllPathsHelper(caveMap, cave, path, paths, visited):
    for c in caveMap[cave].connections:
        if c in visited and visited[c]:
            continue
        path.append(c)
        if not caveMap[c].isBig:
            visited[c] = True
        if c == 'end':
            paths.append(path.copy())
        else:
            findAllPathsHelper(caveMap, c, path, paths, visited)
        visited[path.pop()] = False
    return paths

def part1(path):
    caveMap = buildCaveMap(path)
    return len(findAllPaths(caveMap))

def part2(path):
    pass

if __name__ == '__main__':
    path = 'Day12/input.txt'
    # Part 1: 4104
    print(part1(path))
    # Part 2: 
    print(part2(path))