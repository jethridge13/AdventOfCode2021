import Day6
import unittest

path = 'Day6/example.txt'

class Test(unittest.TestCase):

    def testFishSimulate(self):
        fish = Day6.Fish('3,4,3,1,2')
        self.assertEqual(sum(fish.fish), 5)
        self.assertListEqual(fish.fish, [0,1,1,2,1,0,0,0,0,0])
        fish.simulate(1)
        self.assertEqual(sum(fish.fish), 5)
        self.assertListEqual(fish.fish, [1,1,2,1,0,0,0,0,0,0])
        fish.simulate(1)
        self.assertEqual(sum(fish.fish), 6)
        self.assertListEqual(fish.fish, [1,2,1,0,0,0,1,0,1,0])
        fish.simulate(8)
        self.assertEqual(sum(fish.fish), 12)
        self.assertListEqual(fish.fish, [3,2,2,1,0,1,1,1,1,0])

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day6.part1(path), 5934)
        self.assertEqual(Day6.part1('Day6/input.txt'), 379114)

    # Part 2 Tests
    def test2(self):
        self.assertEqual(Day6.part2(path), 26984457539)

if __name__ == '__main__':
    unittest.main()