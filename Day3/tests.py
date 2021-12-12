import Day3
import unittest

class Test(unittest.TestCase):

    # Part 1 Tests

    def test1(self):
        self.assertEqual(Day3.part1('Day3/example.txt'), 198)

    # Part 2 Tests
    def test2(self):
        self.assertEqual(Day3.part2('Day3/example.txt'), 230)

    def testCountDigits(self):
        lines = ['001', '010', '000']
        self.assertEqual(Day3.countDigits(0, lines), 0)
        self.assertEqual(Day3.countDigits(1, lines), 1)

    def testGetOxygenRating(self):
        lines = []
        with open('Day3/example.txt', 'r') as f:
            line = f.readline()
            while line:
                lines.append(line)
                line = f.readline()
        self.assertEqual(Day3.getOxygenRating(lines), 23)

    def testGetScrubberRating(self):
        lines = []
        with open('Day3/example.txt', 'r') as f:
            line = f.readline()
            while line:
                lines.append(line)
                line = f.readline()
        self.assertEqual(Day3.getScrubberRating(lines), 10)

if __name__ == '__main__':
    unittest.main()