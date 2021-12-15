import Day12
import unittest

path = 'Day12/example.txt'
path2 = 'Day12/example2.txt'
path3 = 'Day12/example3.txt'

class Test(unittest.TestCase):

    # Part 1 Tests
    def testBuildCaveMap(self):
        caveMap = Day12.buildCaveMap(path)
        self.assertCountEqual(caveMap['start'].connections, ['A', 'b'])
        self.assertCountEqual(caveMap['end'].connections, ['A', 'b'])
        self.assertCountEqual(caveMap['A'].connections, ['start', 'b', 'c', 'end'])
        self.assertCountEqual(caveMap['b'].connections, ['start', 'end', 'A', 'd'])
        self.assertCountEqual(caveMap['c'].connections, ['A'])
        self.assertCountEqual(caveMap['d'].connections, ['b'])
        caveMap = Day12.buildCaveMap(path2)
        self.assertCountEqual(caveMap['start'].connections, ['HN', 'kj', 'dc'])
        self.assertCountEqual(caveMap['end'].connections, ['dc','HN'])

    def testFindAllPaths(self):
        caveMap = Day12.buildCaveMap(path)
        ans =   [['start','A','b','A','c','A','end'],
                ['start','A','b','A','end'],
                ['start','A','b','end'],
                ['start','A','c','A','b','A','end'],
                ['start','A','c','A','b','end'],
                ['start','A','c','A','end'],
                ['start','A','end'],
                ['start','b','A','c','A','end'],
                ['start','b','A','end'],
                ['start','b','end']]
        result = Day12.findAllPaths(caveMap)
        self.assertCountEqual(result, ans)

    def test1(self):
        self.assertEqual(Day12.part1(path), 10)
        self.assertEqual(Day12.part1(path2), 19)
        self.assertEqual(Day12.part1(path3), 226)

    # Part 2 Tests
    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main()