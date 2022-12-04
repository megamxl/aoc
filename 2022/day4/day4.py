input = "2022/day4/input.txt"
smallInput = "2022/day4/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n').split(",") for line in puzzle_input.readlines()]

def part1(sum, sum2, list):
    for paris in list:
        curr = [paris[0].split("-"), paris[1].split("-")]
        set1, set2 = set(range(int(curr[0][0]),int(curr[0][1])+1)), set(range(int(curr[1][0]),int(curr[1][1])+1))
        if set1.issubset(set2) or set2.issubset(set1): sum += 1
        if min(set1) <= max(set2) and min(set2) < min(set1) or min(set2) <= max(set1) and min(set1) <= min(set2): sum2 +=1
    return [sum,sum2]

print(f'challange 1 and 2: {part1(0,0,testCase)}')