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
                board = createBoard(temp)
                boards.append(board)
                temp = []
            else:
                temp.append(line.split())
            line = f.readline()
        board = createBoard(temp)
        boards.append(board)
    return boards, calls

def createBoard(board):
    pass

def part1(path):
    pass

def part2(path):
    pass

if __name__ == '__main__':
    # Part 1: 
    print(part1('Day4/input.txt'))
    # Part 2: 
    print(part2('Day4/input.txt'))