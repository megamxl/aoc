
input = "2022/day3/input.txt"
smallInput = "2022/day3/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n') for line in puzzle_input.readlines()]

def part1(sum, list):
    for currElemnt in list:
        half  = int(((len(currElemnt))/2))
        str1 = currElemnt[0: half]
        str2 = currElemnt[half:]
        for currChar in str1:
            if currChar in str2:
                sum += addToProTOSum(currChar)
                break
    return sum

def addToProTOSum(currChar):
    if  ord(currChar) > 96:
        return ord( currChar) - 96
    else:
        return ord(currChar) -38

def part2(sum, list):
    for currElemnt in range(0,len(list),3):
        for currChar in list[currElemnt]:
            if currChar in list[currElemnt+1] and currChar in list[currElemnt+2]:
                    sum += addToProTOSum(currChar)
                    break
    return sum



print(f'challange 1 {part1(0,testCase)}')
print(f'challange 2 {part2(0,testCase)}')