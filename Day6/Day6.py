class Fish:

    def __init__(self, line):
        fish = list(map(int, line.split(',')))
        self.fish = [0] * 10
        for i in fish:
            self.fish[i] += 1

    def simulate(self, n):
        for i in range(n):
            for index, fish in enumerate(self.fish):
                if index == 0:
                    self.fish[9] += fish
                    self.fish[7] += fish
                else:
                    self.fish[index-1] = fish
            self.fish[-1] = 0

def part1(path):
    with open(path, 'r') as f:
        line = f.readline()
        fish = Fish(line)
    fish.simulate(80)
    return sum(fish.fish)

def part2(path):
    with open(path, 'r') as f:
        line = f.readline()
        fish = Fish(line)
    fish.simulate(256)
    return sum(fish.fish)

if __name__ == '__main__':
    path = 'Day6/input.txt'
    # Part 1: 379114
    print(part1(path))
    # Part 2: 1702631502303
    print(part2(path))