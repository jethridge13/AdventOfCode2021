import Day8
import unittest

path = 'Day8/example.txt'

class Test(unittest.TestCase):

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day8.part1(path), 26)

    # Part 2 Tests
    def testDecode(self):
        inp = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
        out = {
            'abcdefg': 8,
            'bcdef': 5,
            'acdfg': 2,
            'abcdf': 3,
            'abd': 7,
            'abcdef': 9,
            'bcdefg': 6,
            'abef': 4,
            'abcdeg': 0,
            'ab': 1
        }
        self.assertDictEqual(Day8.decode(inp.split()), out)

    def test2(self):
        self.assertEqual(Day8.part2(path), 61229)

if __name__ == '__main__':
    unittest.main()