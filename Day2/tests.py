import Day2
import unittest

class Test(unittest.TestCase):

    # Part 1 Tests
    def parseLineTest(self):
        vector, magnitude = Day2.parseLine('forward 5')
        self.assertEqual(vector, 'forward')
        self.assertEqual(magnitude, 5)

        vector, magnitude = Day2.parseLine('backward, 3')
        self.assertEqual(vector, 'backward')
        self.assertEqual(magnitude, 3)

    def test1(self):
        self.assertEqual(Day2.part1('Day2/example.txt'), 150)

    # Part 2 Tests
    def test2(self):
        self.assertEqual(Day2.part2('Day2/example.txt'), 900)

if __name__ == '__main__':
    unittest.main()