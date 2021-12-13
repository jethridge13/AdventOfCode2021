import Day7
import unittest

path = 'Day7/example.txt'

class Test(unittest.TestCase):

    # Part 1 Tests
    def testCalcFuel(self):
        l = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(Day7.calcFuel(l, 2), 37)
        self.assertEqual(Day7.calcFuel(l, 1), 41)
        self.assertEqual(Day7.calcFuel(l, 3), 39)
        self.assertEqual(Day7.calcFuel(l, 10), 71)

    def testCalcTotalFuel(self):
        l = [16,1,2,0,4,2,7,1,2,14]
        self.assertListEqual(Day7.calcTotalFuel(l), [49, 41, 37, 39, 41, 45, 49, 53, 59, 65, 71, 77, 83, 89, 95, 103])

    def testFindOptimalFuel(self):
        l = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(Day7.findOptimalFuel(l), 37)
        with open(path, 'r') as f:
            line = f.readline()
            l = list(map(int, line.split(',')))
        self.assertEqual(Day7.findOptimalFuel(l), 352997)

    def test1(self):
        self.assertEqual(Day7.part1(path), 37)

    # Part 2 Tests
    def testCalcFuel2(self):
        l = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(Day7.calcFuel2(l, 5), 168)
        self.assertEqual(Day7.calcFuel2(l, 2), 206)

    def test2(self):
        self.assertEqual(Day7.part2(path), 168)

if __name__ == '__main__':
    unittest.main()