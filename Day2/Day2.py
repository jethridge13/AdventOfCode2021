def parseline(line):
    parts = line.split(' ')
    magnitude = int(parts[1])
    return parts[0], magnitude

def part1(path):
    horizontal = 0
    depth = 0
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            vector, magnitude = parseline(line)
            if vector == 'forward':
                horizontal += magnitude
            elif vector == 'up':
                depth -= magnitude
            elif vector == 'down':
                depth += magnitude
            else:
                print(line)
            line = f.readline()
    return horizontal * depth

def part2(path):
    horizontal = 0
    depth = 0
    aim = 0
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            vector, magnitude = parseline(line)
            if vector == 'forward':
                horizontal += magnitude
                depth += aim * magnitude
            elif vector == 'up':
                aim -= magnitude
            elif vector == 'down':
                aim += magnitude
            else:
                print(line)
            line = f.readline()
    return horizontal * depth

if __name__ == '__main__':
    # Part 1: 1727835
    print(part1('Day2/input.txt'))
    # Part 2: 1544000595
    print(part2('Day2/input.txt'))