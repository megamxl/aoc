input = "2022/day6/input.txt"
smallInput = "2022/day6/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n').split(",") for line in puzzle_input.readlines()]

def part1(sum, sum2, list):

    return [sum,sum2]

print(f'challange 1 and 2: {part1(0,0,testCase)}')