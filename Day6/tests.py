import Day6
import unittest

path = 'Day6/example.txt'

class Test(unittest.TestCase):

    def testFishSimulate(self):
        fish = Day6.Fish('3,4,3,1,2')
        self.assertListEqual(fish.fish, [3,4,3,1,2])
        fish.simulate(1)
        self.assertListEqual(fish.fish, [2,3,2,0,1])
        fish.simulate(1)
        self.assertListEqual(fish.fish, [1,2,1,6,0,8])
        fish.simulate(8)
        self.assertListEqual(fish.fish, [0,1,0,5,6,0,1,2,2,3,7,8])

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day6.part1(path), 5934)
        self.assertEqual(Day6.part1('Day6/input.txt'), 379114)

    # Part 2 Tests
    def test2(self):
        # self.assertEqual(Day6.part2(path), 26984457539)
        pass

if __name__ == '__main__':
    unittest.main()