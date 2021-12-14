import Day9
import unittest

path = 'Day9/example.txt'

class Test(unittest.TestCase):

    # Part 1 Tests
    def testGenerateGrid(self):
        l = [[2,1,9,9,9,4,3,2,1,0],
            [3,9,8,7,8,9,4,9,2,1],
            [9,8,5,6,7,8,9,8,9,2],
            [8,7,6,7,8,9,6,7,8,9],
            [9,8,9,9,9,6,5,6,7,8]]
        self.assertListEqual(Day9.generateGrid(path), l)

    def testFindLowPoints(self):
        grid = Day9.generateGrid(path)
        ans = {(0, 1): 1, (0, 9): 0, (2, 2): 5, (4, 6): 5}
        self.assertDictEqual(Day9.findLowPoints(grid), ans)

    def testCalcRisk(self):
        lowPoints = {(0, 1): 1, (0, 9): 0, (2, 2): 5, (4, 6): 5}
        self.assertEqual(Day9.calcRisk(lowPoints), 15)

    def test1(self):
        self.assertEqual(Day9.part1(path), 15)

    # Part 2 Tests
    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main()