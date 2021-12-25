
with open("day10\input.txt") as puzzle_input:
    puzzle_input = [[nums.split(" ") for nums in line.rstrip("\n").split(" | ") ]for line in puzzle_input.readlines()]
    #print(puzzle_input)

isOpening = lambda x: True if x == '(' or x == '[' or x == '{' or x == '<' else False
   
def partOne(lines): 
    
    closingPair ={
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<"
    }
    
    wrongChars = []
     
    for line in lines:
        for second in line:
            for intervals in second:
                opening =[]
                for chars in intervals:
                    if(isOpening(chars)):
                        opening.append(chars)
                    else:
                        lastOpening= opening.pop()
                        if(closingPair[chars] != lastOpening):
                            wrongChars.append(chars)
                            break
    count =0
    for illCahar in wrongChars:
        if(illCahar == ")"):
            count +=3
        elif(illCahar == "]"):
            count +=57
        elif(illCahar == "}"): 
            count+= 1197
        elif(illCahar == ">"):
            count += 25137
    return count
                
def partTow(lines, puz):
   pass

if __name__ == '__main__':
    print(f"part one {partOne(puzzle_input)} ")
    #partTow(puzzle_input)
    pass
