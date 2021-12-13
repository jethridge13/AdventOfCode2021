class Board:

    def __init__(self, board):
        self.board = board
        # Numbers maps values on the board to their location on their board
        # This makes searching the board for numbers much faster
        self.numbers = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.numbers[board[i][j]] = (i, j)
        self.rows = {}
        self.columns = {}
        self.lastMark = 0
        self.marked = []

    def mark(self, n):
        if n in self.numbers:
            self.marked.append(int(n))
            i, j = self.numbers[n]
            if i not in self.rows:
                self.rows[i] = 0
            self.rows[i] += 1
            if j not in self.columns:
                self.columns[j] = 0
            self.columns[j] += 1
            if self.rows[i] == 5 or self.columns[j] == 5:
                return True
        return False

    def calcScore(self):
        s = 0
        for i in self.board:
            for j in i:
                s += int(j)
        s -= sum(self.marked)
        return s * self.marked[-1]

def parseInput(path):
    boards = []
    calls = []
    with open(path, 'r') as f:
        line = f.readline()
        calls = line.replace('\n', '').split(',')
        line = f.readline()
        temp = []
        while line:
            if len(line) == 1 and len(temp) > 0:
                board = Board(temp)
                boards.append(board)
                temp = []
            else:
                temp.append(line.split())
            line = f.readline()
        board = Board(temp)
        boards.append(board)
    return boards, calls

def getWinningBoard(boards, calls):
    for call in calls:
        for board in boards:
            if board.mark(call):
                return board.calcScore()
    return -1

def part1(path):
    boards, calls = parseInput(path)
    return getWinningBoard(boards, calls)

def part2(path):
    pass

if __name__ == '__main__':
    # Part 1: 41668
    print(part1('Day4/input.txt'))
    # Part 2: 
    print(part2('Day4/input.txt'))