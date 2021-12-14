import Day10
import unittest

path = 'Day10/example.txt'

class Test(unittest.TestCase):

    # Part 1 Tests
    def testCalcScore(self):
        scores = {')': 2, ']': 1, '}': 1, '>': 1}
        self.assertEqual(Day10.calcScore(scores), 26397)

    def testScanLine(self):
        line = '{([(<{}[<>[]}>{[]{[(<()>'
        self.assertEqual(Day10.scanLine(line), '}')
        line = '[[<[([]))<([[{}[[()]]]'
        self.assertEqual(Day10.scanLine(line), ')')
        line = '[{[{({}]{}}([{[{{{}}([]'
        self.assertEqual(Day10.scanLine(line), ']')
        line = '[<(<(<(<{}))><([]([]()'
        self.assertEqual(Day10.scanLine(line), ')')
        line = '<{([([[(<>()){}]>(<<{{'
        self.assertEqual(Day10.scanLine(line), '>')

    def test1(self):
        self.assertEqual(Day10.part1(path), 26397)

    # Part 2 Tests
    def testCalcScore2(self):
        line = '}}]])})]'
        self.assertEqual(Day10.calcScore2(line), 288957)
        line = ')}>]})'
        self.assertEqual(Day10.calcScore2(line), 5566)
        line = '}}>}>))))'
        self.assertEqual(Day10.calcScore2(line), 1480781)
        line = ']]}}]}]}>'
        self.assertEqual(Day10.calcScore2(line), 995444)
        line = '])}>'
        self.assertEqual(Day10.calcScore2(line), 294)

    def testFixLine(self):
        line = '[({(<(())[]>[[{[]{<()<>>'
        self.assertEqual(Day10.fixLine(line), '}}]])})]')
        line = '[(()[<>])]({[<{<<[]>>('
        self.assertEqual(Day10.fixLine(line), ')}>]})')
        line = '(((({<>}<{<{<>}{[]{[]{}'
        self.assertEqual(Day10.fixLine(line), '}}>}>))))')
        line = '{<[[]]>}<{[{[{[]{()[[[]'
        self.assertEqual(Day10.fixLine(line), ']]}}]}]}>')
        line = '<{([{{}}[<[[[<>{}]]]>[]]'
        self.assertEqual(Day10.fixLine(line), '])}>')

    def test2(self):
        self.assertEqual(Day10.part2(path), 288957)

if __name__ == '__main__':
    unittest.main()