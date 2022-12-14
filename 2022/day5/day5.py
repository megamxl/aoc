from copy import deepcopy

input = "2022/day5/input.txt"
smallInput = "2022/day5/smalInput.txt"

with open(input) as puzzle_input:
    testCase = [line.rstrip('\n') for line in puzzle_input.readlines()]

def move(amount, wrongStart, wrongEnd, stacks):
    start = int(wrongStart) -1
    end = int(wrongEnd) -1

    for i in range(int(amount)):
        swap = (stacks[start][0])
        stacks[start].remove(swap)
        stacks[end].insert(0,swap)
    return(stacks)

def moveAtOnce(amount, wrongStart, wrongEnd, stacks):
    start = int(wrongStart) -1
    end = int(wrongEnd) -1

    swapList = []
    for i in range(int(amount)):
        swap = (stacks[start][0])
        stacks[start].remove(swap)
        swapList.append(swap)
        i= 0
    for element in swapList:
        stacks[end].insert(i,element) 
        i = i+1
    
    return(stacks)

def part1(list):
    splitter = 0
    for x in range(0,len(list)):
        if "1" in list[x]:
            splitter = x
            break 
    movedInput = []
    for curr in range(len(list[:splitter])):
        result = []
        for i in range(0, len(list[:splitter][curr]), 4):
            result.append(list[:splitter][curr][i : i + 4])
        movedInput.append(result)

    stacks = []
    i = 0
    for m in range(len(movedInput[0])):
        stack = []
        for element in movedInput:
            if element[i][1] != ' ':
                stack.append(element[i][1])
        i+= 1
        stacks.append(stack)
        print(" ")
    print(*stacks, sep="\n")

    moves = list[splitter+2:]
    cur =[line.split(" ") for line in moves]
    for t in cur:
        for m in t:
            if len(m) > 1:
                t.remove(m)
            else:
                m = int(m)

    day1Stacks = deepcopy(stacks)
    day2Stacks = deepcopy(stacks)
    for tmp in cur:
        day1Stacks = move(tmp[0],tmp[1],tmp[2],day1Stacks)
        day2Stacks = moveAtOnce(tmp[0],tmp[1],tmp[2],day2Stacks)
    result = ""
    for r in day1Stacks:
        result += r[0]
    result2 = ""
    for r in day2Stacks:
        result2 += r[0]
    return [result,result2]



print(f'challange 1 and 2: {part1(testCase)}')