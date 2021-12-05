import Day1
import unittest

class Test(unittest.TestCase):

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day1.part1('Day1/example.txt'), 7)

if __name__ == '__main__':
    unittest.main()