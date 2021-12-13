class Board:

    def __init__(self):
        self.board = []

    def addLateralLine(self, start, end):
        highestCoord = max(start + end)
        if highestCoord > len(self.board):
            self.expandBoard(highestCoord)
        # TODO
    
    def expandBoard(self, n):
        if n < len(self.board):
            return
        startingLength = len(self.board)
        newline = [0] * n
        diff = [0] * (n - len(self.board))
        for i in range(n - startingLength):
            self.board.append(newline)
        if startingLength == 0:
            return
        for i in range(len(self.board) - startingLength):
            self.board[i] += diff

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

def part1(path):
    board = Board()
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            start, end = parseLine(line)
            board.addLine(start, end)
            line = f.readline()
    return board.countDuplicateLines(2)

def part2(path):
    pass

if __name__ == '__main__':
    path = 'Day5/input.txt'
    # Part 1: 
    print(part1(path))
    # Part 2: 
    print(part2(path))