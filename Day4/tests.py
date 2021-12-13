import Day4
import unittest

class Test(unittest.TestCase):

    # Part 1 Tests
    def testParseInput(self):
        boards, calls = Day4.parseInput('Day4/example.txt')
        self.assertEqual(len(boards), 3)
        self.assertListEqual(calls, ['7','4','9','5','11','17','23','2','0','14','21','24','10','16','13','6','15','25','12','22','18','20','8','19','3','26','1'])

    def test1(self):
        self.assertEqual(Day4.part1('Day4/example.txt'), 4512)

    # Part 2 Tests
    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main()