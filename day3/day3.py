from os import path


with open("day3\smalInput.txt") as puzzle_input:
    testCase = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]
    #print(testCase)

with open("day3\input.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]
    #print(puzzle_input)
    
result = []
secondlist =  testCase

def partOne(lines):
    helpMe =""
    cont1 = 0
    inverse_s =""
    for j in range (len(lines[0][0])):
            adding = ""
            for i in range(len(lines)):
                adding += str(lines[i][0][cont1])
            result.append(adding)
            cont1 +=1
    for string in result:
        zero =0
        one =0
        for char in string:
            if char == "0":
                zero +=1
            else:
                one +=1
        if(one > zero or one == zero):
            helpMe += "1"
        else:
            helpMe += "0"  
    for i in helpMe:
        if i == '0':
            inverse_s += '1'
        else:
            inverse_s += '0'
    print(int(helpMe,2)* int(inverse_s,2))
            
def findMoreUsed(lines, currentrow):
    cont1 = 0
    contZero =0
    contOne=0
    adding = ""
    searchingChar = "0"
    for j in range (len(lines)):
        adding += str(lines[j][0][currentrow])
    cont1 +=1
    for i in adding:
        if i == '0':
            contZero += 1
        else:
            contOne += 1
    if(contOne > contZero or contZero == contOne):
        searchingChar = '1'
    return searchingChar
        
            
#partOne(testCase)
def filter_nums(nums, rating):
    pos = 0
    while len(nums) > 1:
        ones, zero = [], []
        for num in nums:
            if num[pos] == '1':
                ones.append(num)
            else:
                zero.append(num)
        pos += 1
        by_size = sorted((zero, ones), key=len)
        nums = by_size[1] if rating == 'O2' else by_size[0]
    return int(nums[0], 2)

def part2():
    with open("day3\input.txt", 'r') as f:
        nums = f.read().splitlines() # list with all numbers
    return print(filter_nums(nums, 'O2') * filter_nums(nums, 'CO2'))

part2()