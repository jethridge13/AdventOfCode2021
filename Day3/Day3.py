def part1(path):
    gamma = 0
    epsilon = 0
    linecount = 0
    with open(path, 'r') as f:
        line = f.readline()
        bitcount = [0] * (len(line) - 1)
        while line:
            linecount += 1
            for index, val in enumerate(line):
                if val == '1':
                    bitcount[index] += 1
            line = f.readline()
        gammabits, epsilonbits = '', ''
        half = linecount // 2
        for i in bitcount:
            if i > half:
                gammabits += '1'
                epsilonbits += '0'
            else:
                gammabits += '0'
                epsilonbits += '1'
        gamma, epsilon = int(gammabits, 2), int(epsilonbits, 2)
    return gamma * epsilon

def countDigits(index, lines):
    count = 0
    for i in lines:
        if i[index] == '1':
            count += 1
    return count

def getOxygenRating(lines):
    index = 0
    while len(lines) > 1:
        count = countDigits(index, lines)
        digit = '0'
        if count >= len(lines) - count:
            digit = '1'
        lines = list(filter(lambda line: line[index] == digit, lines))
        index += 1
    return int(lines[0], 2)

def getScrubberRating(lines):
    index = 0
    while len(lines) > 1:
        count = countDigits(index, lines)
        digit = '1'
        if count >= len(lines) - count:
            digit = '0'
        lines = list(filter(lambda line: line[index] == digit, lines))
        index += 1
    return int(lines[0], 2)

def part2(path):
    lines = []
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    oxygen = getOxygenRating(lines)
    scrubber = getScrubberRating(lines)
    return oxygen * scrubber

if __name__ == '__main__':
    # Part 1: 2583164
    print(part1('Day3/input.txt'))
    # Part 2: 2784375
    print(part2('Day3/input.txt'))