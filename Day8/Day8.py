def part1(path):
    count = 0
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            parts = line.split(' | ')
            words = parts[1].split()
            for word in words:
                l = len(word)
                if l == 2 or l == 3 or l == 4 or l == 7:
                    count += 1
            line = f.readline()
    return count

def decode(examples):
    segments = {}
    segmentsR = {}
    unsorted = {}
    # Find 1, 4, 7, 8 and collect the rest by length of display
    for i in examples:
        if len(i) == 2:
            segments["".join(sorted(i))] = 1
            segmentsR[1] = i
        elif len(i) == 3:
            segments["".join(sorted(i))] = 7
            segmentsR[7] = i
        elif len(i) == 4:
            segments["".join(sorted(i))] = 4
            segmentsR[4] = i
        elif len(i) == 7:
            segments["".join(sorted(i))] = 8
            segmentsR[8] = i
        else:
            if len(i) not in unsorted:
                unsorted[len(i)] = []
            unsorted[len(i)].append(i)
    # Find 2
    four = set(list(segmentsR[4]))
    for i in unsorted[5]:
        s = set(list(i))
        if len(s - four) == 3:
            segments["".join(sorted(i))] = 2
            segmentsR[2] = i
            unsorted[5].remove(i)
            break
    # Find 3
    one = set(list(segmentsR[1]))
    for i in unsorted[5]:
        s = set(list(i))
        if len(s - one) == 3:
            segments["".join(sorted(i))] = 3
            segmentsR[3] = i
            unsorted[5].remove(i)
            break
    # Remaining 5-length word is 5
    five = unsorted[5].pop()
    segments["".join(sorted(five))] = 5
    segmentsR[5] = five
    # Find 9
    for i in unsorted[6]:
        s = set(list(i))
        if set.union(set(list(segmentsR[4])), set(list(segmentsR[3]))) == s:
            segments["".join(sorted(i))] = 9
            segmentsR[9] = i
            unsorted[6].remove(i)
            break
    # Find 0
    five = set(list(segmentsR[5]))
    for i in unsorted[6]:
        s = set(list(i))
        if len(s - five) == 2:
            segments["".join(sorted(i))] = 0
            segmentsR[0] = i
            unsorted[6].remove(i)
            break
    # Remaining 6-length word is 6
    six = unsorted[6].pop()
    segments["".join(sorted(six))] = 6
    segmentsR[6] = six
    return segments

def part2(path):
    total = 0
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            parts = line.split(' | ')
            digits = decode(parts[0].split())
            scoreDigits = parts[1].split()
            value = ''
            for digit in scoreDigits:
                value += str(digits["".join(sorted(digit))])
            total += int(value)
            line = f.readline()
    return total

if __name__ == '__main__':
    path = 'Day8/input.txt'
    # Part 1: 412
    print(part1(path))
    # Part 2: 978171
    print(part2(path))