def calcScore(scoreCount):
    scoreMap = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = scoreCount[')'] * scoreMap[')'] + \
        scoreCount[']'] * scoreMap[']'] + \
        scoreCount['}'] * scoreMap['}'] + \
        scoreCount['>'] * scoreMap['>']
    return score

def calcScore2(scoreLine):
    scoreMap = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for c in scoreLine:
        score *= 5
        score += scoreMap[c]
    return score

def scanLine(line):
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
        else:
            p = stack.pop()
            if (p == '(' and c != ')') or \
                (p == '[' and c != ']') or \
                (p == '{' and c != '}') or \
                (p == '<' and c != '>'):
                return c
    return None

def fixLine(line):
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
        else:
            p = stack.pop()
            if (p == '(' and c != ')') or \
                (p == '[' and c != ']') or \
                (p == '{' and c != '}') or \
                (p == '<' and c != '>'):
                return None
    s = ''
    stack.reverse()
    for c in stack:
        if c == '(':
            s += ')'
        elif c == '[':
            s += ']'
        elif c == '{':
            s += '}'
        else:
            s += '>'
    return s

def part1(path):
    brackets = {')': 0, ']': 0, '}': 0, '>': 0}
    with open(path, 'r') as f:
        line = f.readline().replace('\n', '')
        while line:
            c = scanLine(line)
            if c:
                brackets[c] += 1
            line = f.readline().replace('\n', '')
    return calcScore(brackets)

def part2(path):
    strings = []
    with open(path, 'r') as f:
        line = f.readline().replace('\n', '')
        while line:
            string = fixLine(line)
            if string:
                strings.append(string)
            line = f.readline().replace('\n', '')
    scores = []
    for s in strings:
        scores.append(calcScore2(s))
    scores.sort()
    return scores[len(scores) // 2]

if __name__ == '__main__':
    path = 'Day10/input.txt'
    # Part 1: 216297
    print(part1(path))
    # Part 2: 2165057169
    print(part2(path))