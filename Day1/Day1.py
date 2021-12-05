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

def part2(path):
    with open(path, 'r') as f:
        line = f.readline()
        count = 0
        prev = None
        group = []
        while line:
            line = int(line)
            group.append(line)
            if len(group) == 4:
                group.pop(0)
            if len(group) == 3:
                s = sum(group)
                if not prev:
                    prev = s
                else:
                    if s > prev:
                        count += 1
                prev = s
            line = f.readline()
    return count

if __name__ == '__main__':
    # Part 1: 1791
    print(part1('Day1/Day1.txt'))
    # Part 2: 1822
    print(part2('Day1/Day1.txt'))