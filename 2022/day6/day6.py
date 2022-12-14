from collections import Counter


input = "/Users/mopedmaxl/PycharmProjects/aoc/2022/day6/input.txt"
smallInput = "/Users/mopedmaxl/PycharmProjects/aoc/2022/day6/smalInput.txt"

with open(smallInput) as puzzle_input:
    testCase = [line.rstrip('\n') for line in puzzle_input.readlines()]


def isUniqueChars(string):
    freq = Counter(string)
    if (len(freq) == len(string)):
        return True
    else:
        return False
def part1(list):
    for line in list:
        for (start, element) enumerate(line):
        start = 0
        end = 4
        if isUniqueChars()
        start += 1
        end += 1

print(f'challange 1 and 2: {part1(testCase)}')