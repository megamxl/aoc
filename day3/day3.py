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

for i in range(len(testCase[0][0])):
    importantChar = findMoreUsed(testCase,i)
    for r in range(len(testCase)):
        if(secondlist[r][0][i] != importantChar):
            del secondlist[r][0]
print(secondlist)
