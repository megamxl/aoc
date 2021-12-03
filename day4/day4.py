from os import path


with open("day4\smalInput.txt") as puzzle_input:
    testCase = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]
    #print(testCase)

with open("day4\input.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]
    #print(puzzle_input)
    
    
with open("day4\smalInput.txt", 'r') as f:
        nums = f.read().splitlines() # list with all numbers

print(nums)    
def part1(lines):
    print("hey")

def part2(lines):
    print("hey")

part1(testCase)
part2()
