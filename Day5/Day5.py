class Board:

    def __init__(self):
        self.board = []

    def addLine(self, start, end):
        start = start.copy()
        highestCoord = max(start + end)
        if highestCoord > len(self.board):
            self.expandBoard(highestCoord+1)
        xinc = 1
        yinc = 1
        if start[0] == end[0]:
            xinc = 0
        elif start[0] > end[0]:
            xinc = -1
        if start[1] == end[1]:
            yinc = 0
        elif start[1] > end[1]:
            yinc = -1
        while start[0] != end[0] or start[1] != end[1]:
            self.board[start[0]][start[1]] += 1
            start[0] += xinc
            start[1] += yinc
        self.board[start[0]][start[1]] += 1
    
    def expandBoard(self, n):
        if n < len(self.board):
            return
        startingLength = len(self.board)
        for i in range(n - startingLength):
            self.board.append([0] * n)
        if startingLength == 0:
            return
        for i in range(len(self.board) - (len(self.board) - startingLength)):
            self.board[i] += ([0] * (n - startingLength))

    def countDuplicateLines(self, n):
        count = 0
        for i in self.board:
            for j in i:
                if j >= n:
                    count += 1
        return count

def parseLine(line):
    parts = line.split(' -> ')
    start = parts[0].split(',')
    end = parts[1].split(',')
    start = [int(x) for x in start]
    end = [int(x) for x in end]
    return start, end

# True if line is horizontal or vertical, False if diagonal
def lineIsAxial(start, end):
    return start[0] == end[0] or start[1] == end[1]

def part1(path):
    board = Board()
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            start, end = parseLine(line)
            if lineIsAxial(start, end):
                board.addLine(start, end)
            line = f.readline()
    return board.countDuplicateLines(2)

def part2(path):
    board = Board()
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            start, end = parseLine(line)
            board.addLine(start, end)
            line = f.readline()
    return board.countDuplicateLines(2)

if __name__ == '__main__':
    path = 'Day5/input.txt'
    # Part 1: 6189
    print(part1(path))
    # Part 2: 19164
    print(part2(path))