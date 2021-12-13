def calcFuel(l, n):
    cost = 0
    for i in l:
        cost += abs(i - n)
    return cost

def calcFuel2(l, n):
    cost = 0
    for i in l:
        diff = abs(i - n)
        cost += (diff ** 2 + diff) // 2
    return cost

def calcTotalFuel(l, part2=False):
    costs = []
    for i in range(max(l)):
        if part2:
            costs.append(calcFuel2(l, i))
        else:
            costs.append(calcFuel(l, i))
    return costs

def findOptimalFuel(l, part2=False):
    return min(calcTotalFuel(l, part2))
    '''
    # Initial binary search attempt that didn't quite work out fully
    lo, hi = min(l), max(l)
    while lo < hi:
        if part2:
            loFuel = calcFuel2(l, lo)
            hiFuel = calcFuel2(l, hi)
            mid = (hi + lo) // 2
            midFuel = calcFuel2(l, mid)
        else:
            loFuel = calcFuel(l, lo)
            hiFuel = calcFuel(l, hi)
            mid = (hi + lo) // 2
            midFuel = calcFuel(l, mid)
        if loFuel < midFuel and midFuel < hiFuel:
            hi = mid
        elif loFuel > midFuel and midFuel > hiFuel:
            lo = mid
        elif hiFuel > loFuel:
            hi -= 1
        else:
            lo += 1
    return lo
    '''

def part1(path):
    with open(path, 'r') as f:
        line = f.readline()
        l = list(map(int, line.split(',')))
    return findOptimalFuel(l)

def part2(path):
    with open(path, 'r') as f:
        line = f.readline()
        l = list(map(int, line.split(',')))
    return findOptimalFuel(l, part2=True)

if __name__ == '__main__':
    path = 'Day7/input.txt'
    # Part 1: 352997
    print(part1(path))
    # Part 2: 101571302
    print(part2(path))