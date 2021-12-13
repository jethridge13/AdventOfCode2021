import Day5
import unittest

path = 'Day5/example.txt'

class Test(unittest.TestCase):

    def parseLineTest(self):
       start, end = Day5.parseLine('0,9 -> 5,9')
       self.assertListEqual(start, [0,9])
       self.assertListEqual(end, [5,9])

    def testBoardExandBoard(self):
        start, end = Day5.parseLine('0,9 -> 5,9')
        board = Day5.Board()
        board.expandBoard(3)
        self.assertListEqual(board.board, [[0,0,0],[0,0,0],[0,0,0]])
        board.expandBoard(2)
        self.assertListEqual(board.board, [[0,0,0],[0,0,0],[0,0,0]])
        board.expandBoard(4)
        self.assertListEqual(board.board, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    # Part 1 Tests
    def test1(self):
        self.assertEqual(Day5.part1(path), 5)

    # Part 2 Tests
    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main()