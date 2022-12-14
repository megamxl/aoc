input = "2022/day6/input.txt"
smallInput = "2022/day6/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n') for line in puzzle_input.readlines()]

def isUniqueChars(string):
    char_seen = []
    for char in string:
        if char not in char_seen:
            char_seen.append(char)
    return char_seen

def solver(list, part, sum):
    if part == 1:
        end = 4
        maxsize = 4
    if part == 2:
        end = 14
        maxsize = 14

    for line in list:
        end
        for start in range(len(line)):
            if len(isUniqueChars(line[start:end])) == maxsize: 
                sum += end
                break
            end += 1
    return sum

print(f'challange 1: {solver(testCase,1,0)}')
print(f'challange 2: {solver(testCase,2,0)}')