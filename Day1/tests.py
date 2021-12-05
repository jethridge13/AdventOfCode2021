import Day1
import unittest

class Test(unittest.TestCase):

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day1.part1('Day1/example.txt'), 7)

    # Part 2 Tests
    def test2(self):
        self.assertEqual(Day1.part2('Day1/example.txt'), 5)

if __name__ == '__main__':
    unittest.main()