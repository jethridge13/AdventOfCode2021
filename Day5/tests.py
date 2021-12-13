import Day5
import unittest

path = 'Day5/example.txt'

class Test(unittest.TestCase):

    def parseLineTest(self):
       start, end = Day5.parseLine('0,9 -> 5,9')
       self.assertListEqual(start, [0,9])
       self.assertListEqual(end, [5,9])

    def testBoardExandBoard(self):
        board = Day5.Board()
        board.expandBoard(3)
        self.assertListEqual(board.board, [[0,0,0],[0,0,0],[0,0,0]])
        board.expandBoard(2)
        self.assertListEqual(board.board, [[0,0,0],[0,0,0],[0,0,0]])
        board.expandBoard(4)
        self.assertListEqual(board.board, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    def testBoardAddLine(self):
        board = Day5.Board()
        start, end = Day5.parseLine('0,0 -> 0,2')
        board.addLine(start, end)
        self.assertListEqual(board.board, [[1,1,1],[0,0,0],[0,0,0]])
        board.addLine(start, end)
        self.assertListEqual(board.board, [[2,2,2],[0,0,0],[0,0,0]])
        start, end = Day5.parseLine('0,0 -> 2,0')
        board.addLine(start, end)
        self.assertListEqual(board.board, [[3,2,2],[1,0,0],[1,0,0]])

    def testLineIsAxial(self):
        start, end = Day5.parseLine('0,9 -> 5,9')
        self.assertTrue(Day5.lineIsAxial(start, end))
        start, end = Day5.parseLine('8,0 -> 0,8')
        self.assertFalse(Day5.lineIsAxial(start, end))
        start, end = Day5.parseLine('6,4 -> 2,0')
        self.assertFalse(Day5.lineIsAxial(start, end))

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day5.part1(path), 5)

    # Part 2 Tests
    def test2(self):
        self.assertEqual(Day5.part2(path), 12)

if __name__ == '__main__':
    unittest.main()