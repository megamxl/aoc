input = "2022/day4/input.txt"
smallInput = "2022/day4/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n').split(",") for line in puzzle_input.readlines()]

def part1(sum, list):
    for paris in list:
        curr = [paris[0].split("-"), paris[1].split("-")]
        if isInRange(int(curr[0][0]), int(curr[0][1]), int(curr[1][0]), int(curr[1][1])): sum += 1
    return sum

def part2(sum, list):
    for paris in list:
        curr = [paris[0].split("-"), paris[1].split("-")]
        set1, set2 = set(range(int(curr[0][0]), int(curr[0][1])+1)), set(range(int(curr[1][0]), int(curr[1][1])+1))
        if min(set1) <= max(set2) and min(set2) < min(set1): # part 2
                sum += 1
        if min(set2) <= max(set1) and min(set1) <= min(set2):
                sum += 1
    return sum

def isInRange(x1,y1,x2,y2):
    diff1, diff2 = set(range(x1,y1+1)), set(range(x2,y2+1))
    return diff2.issubset(diff1) or diff1.issubset(diff2)

print(f'challange 1 {part1(0,testCase)}')
print(f'challange 2 {part2(0,testCase)}')