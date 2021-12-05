def part1(path):
    with open(path, 'r') as f:
        line = f.readline()
        prev = None
        count = 0
        while line:
            line = int(line)
            if not prev:
                prev = line
            else:
                if line > prev:
                    count += 1
            prev = line
            line = f.readline()
    return count

if __name__ == '__main__':
    # Part 1: 1791
    print(part1('Day1/Day1.txt'))
    # Part 2:
    #print(part2())