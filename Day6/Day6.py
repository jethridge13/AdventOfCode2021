class Fish:

    def __init__(self, line):
        self.fish = list(map(int, line.split(',')))

    def simulate(self, n):
        for i in range(n):
            for index, fish in enumerate(self.fish):
                if fish == 0:
                    self.fish.append(9)
                    self.fish[index] = 7
                self.fish[index] -= 1

def part1(path):
    with open(path, 'r') as f:
        line = f.readline()
        fish = Fish(line)
    fish.simulate(80)
    return len(fish.fish)

def part2(path):
    with open(path, 'r') as f:
        line = f.readline()
        fish = Fish(line)
    fish.simulate(256)
    return len(fish.fish)

if __name__ == '__main__':
    path = 'Day6/input.txt'
    # Part 1: 379114
    print(part1(path))
    # Part 2: 
    print(part2(path))