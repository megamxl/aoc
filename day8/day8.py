
with open("day8\small.txt") as puzzle_input:
    puzzle_input = [[nums.split(" ") for nums in line.rstrip("\n").split(" | ") ]for line in puzzle_input.readlines()]
    #print(puzzle_input)
 
with open("day8\small.txt") as inPutFoRWierdWay:
    inPutFoRWierdWay = [ line.rstrip("\n").replace("|", "") for line in inPutFoRWierdWay.readlines()]
    inPutFoRWierdWay1 = [line.split(" ") for line in inPutFoRWierdWay]

   
def partOne(lines): 
    cont = 0
    for t in lines:
        for i in t:
            if(len(i)== 4):
                for r in i:
                    if(len(r) == 2 or len(r) == 4 or len(r)  == 7  or len(r)== 3):
                        cont +=1
    print(cont)    


def connectBrain(lines,puz):
    winnerMatrix =[]
    for i in lines:
        winnerMatrix.append(partTow(i, puz))
          
def partTow(lines, puz):
    SevenSegmentDecoded = []
    SevenSegmentDecoded.extend(range(0, 7))
    SevenSegmentDecoded2 = []
    SevenSegmentDecoded2.extend(range(0, 7))
    fixedList= []
    solution = []
    detectedOne = False
    for r in lines:
        if(len(r) == 2):
            rechts1 =r[0]
            rechts2= r[1]
            SevenSegmentDecoded[1] =rechts1
            SevenSegmentDecoded2[1] = rechts2 
            SevenSegmentDecoded[2] =rechts2
            SevenSegmentDecoded2[2] = rechts1 
            detectedOne = True
    for r in lines:
        if(len(r)== 3 and detectedOne):
            s = str(r)
            for m in s:
                if m != rechts1 and m != rechts2:
                    SevenSegmentDecoded[0] = m
                    SevenSegmentDecoded2[0] = m
                        
        
    for r in lines:
        if(len(r) == 6 and SevenSegmentDecoded[1] in r and SevenSegmentDecoded[2] in r):
            if('a' not in r ):
                SevenSegmentDecoded[4] = "a"
                SevenSegmentDecoded2[4] = "a"
            elif("b" not in r ):
                SevenSegmentDecoded[4] = "b"
                SevenSegmentDecoded2[4] = "b"
            elif("c" not in r ):
                SevenSegmentDecoded[4] = "c"
                SevenSegmentDecoded2[4] = "c"
            elif("d" not in r):
                SevenSegmentDecoded[4] = "d"
                SevenSegmentDecoded2[4] = "d"
            elif("e" not in r):
                SevenSegmentDecoded[4] = "e"
                SevenSegmentDecoded2[4] = "e"
            elif("g" not in r):
                SevenSegmentDecoded[4] = "g"
                SevenSegmentDecoded2[4] = "g"
            elif("f" not in r):
                SevenSegmentDecoded[4] = "f"
                SevenSegmentDecoded2[4] = "f"
            if('a' not in r ):
                    if("a" != rechts1 and "a" != rechts2):
                        SevenSegmentDecoded[5]= "a"
                        SevenSegmentDecoded2[5]= "a"
                        continue
            elif('b' not in r ):
                    if("b" != rechts1 and "b" != rechts2):
                        SevenSegmentDecoded[5]= "b"
                        SevenSegmentDecoded2[5]= "b"
                        continue
            elif('c' not in r ):
                    if("c" != rechts1 and "c" != rechts2):
                        SevenSegmentDecoded[5]= "c"
                        SevenSegmentDecoded2[5]= "c"
                        continue
            elif('d' not in r ):
                    if("d" != rechts1 and "d" != rechts2):
                        SevenSegmentDecoded[5]= "d"
                        SevenSegmentDecoded2[5]= "d"
                        continue
            elif('e' not in r ):
                    if("e" != rechts1 and "e" != rechts2):
                        SevenSegmentDecoded[5]= "e"
                        SevenSegmentDecoded2[5]= "e"
                        continue
            elif('g' not in r ):
                    if("g" != rechts1 and "g" != rechts2):
                        SevenSegmentDecoded[5]= "g"
                        SevenSegmentDecoded2[5]= "g"
                        continue
            elif('f' not in r ):
                    if("f" != rechts1 and "f" != rechts2):
                        SevenSegmentDecoded[5]= "f"
                        SevenSegmentDecoded2[5]= "f"
                        continue
        elif(len(r) == 6 ):  
            if('a' not in r ):
                if("a" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("b" not in r ):
                if("b" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("c" not in r ):
                if("c" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("d" not in r):
                if("d" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("e" not in r):
                if("e" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("g" not in r):
                if("g" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
            elif("f" not in r):
                if("a" == rechts1):
                    fixedList = SevenSegmentDecoded.copy()
                else:
                    fixedList = SevenSegmentDecoded2.copy()
    
    for r in lines:
        if(len(r) ==5 ):
            if(fixedList[1] in r and fixedList[2] in r):
                for t in r:
                    if(t != fixedList[1] and t != fixedList[2] and t != fixedList[3] and t!= fixedList[4]):
                        fixedList[3] = t
                        
    for r in lines:
        if(len(r)== 4):
           if(fixedList[1] in r and fixedList[2] in r and fixedList[1] in r ):
               for t in r:
                   if(t != fixedList[1] and t != fixedList[2] and t != fixedList[3]):
                       fixedList[5] = t
    
    why =""
    for n in range(len(fixedList)-1):
        why +=str(fixedList[n])
    if("a" not in why):
        fixedList[6] ="a"
    elif("b" not in why):
        fixedList[6] ="b"
    elif("c" not in why):
        fixedList[6] ="c"
    elif("d" not in why):
        fixedList[6] ="d"
    elif("e" not in why):
        fixedList[6] ="e"
    elif("f" not in why):
        fixedList[6] ="f"
    elif("g" not in why):
        fixedList[6] ="g"
    
    print(fixedList)
    
    zero = fixedList[0] + fixedList[1] + fixedList[2] + fixedList[4] + fixedList[5] + fixedList[6]
    one = fixedList[1] + fixedList[2] 
    tow = fixedList[0] + fixedList[1] + fixedList[3] +  fixedList[4] + fixedList[6] 
    three = fixedList[0] + fixedList[1] + fixedList[3] +  fixedList[2] + fixedList[6] 
    four = fixedList[5] + fixedList[3] + fixedList[2] +  fixedList[1] 
    five = fixedList[0] + fixedList[2] + fixedList[3] +  fixedList[6] +  fixedList[5]
    six = fixedList[0] + fixedList[2] + fixedList[3] +  fixedList[4] +  fixedList[5] +  fixedList[6]
    seven = fixedList[0] + fixedList[1] + fixedList[2]
    eigth = fixedList[0] + fixedList[1] + fixedList[2] + fixedList[3] + fixedList[4] + fixedList[5] + fixedList[6]
    nine = fixedList[0] + fixedList[1] + fixedList[2] + fixedList[3] + fixedList[5] + fixedList[6]
     
     
    sorted_characters = sorted(one)
    one = "".join(sorted_characters)
      
    sorted_characters = sorted(tow)
    tow = "".join(sorted_characters)  
    
    sorted_characters = sorted(three)
    three = "".join(sorted_characters)
    
    sorted_characters = sorted(four)
    four = "".join(sorted_characters)
    
    sorted_characters = sorted(five)
    five = "".join(sorted_characters)
    
    sorted_characters = sorted(six)
    six = "".join(sorted_characters)
    
    sorted_characters = sorted(seven)
    seven = "".join(sorted_characters)
    
    sorted_characters = sorted(eigth)
    eigth = "".join(sorted_characters)
    
    sorted_characters = sorted(nine)
    nine = "".join(sorted_characters)
    
    sorted_characters = sorted(zero)
    zero = "".join(sorted_characters)
    
    count = 0
    for t in puz:
        for i in t:
            if(len(i)== 4):
                apendStr =""
                for r in i:
                    sorted_characters = sorted(str(r))
                    sortedElement = "".join(sorted_characters)
                    print(sortedElement)
                    if(sortedElement == zero):
                        apendStr+="0"
                    elif(sortedElement == one):
                        apendStr+= "1"
                    elif(sortedElement == tow):
                        apendStr+= "2"
                    elif(sortedElement == three):
                        apendStr+= "3"
                    elif(sortedElement == four):
                        apendStr+= "4"
                    elif(sortedElement == five):
                        apendStr+= "5"
                    elif(sortedElement == six):
                        apendStr+= "6"
                    elif(sortedElement == seven):
                        apendStr+= "7"
                    elif(sortedElement == eigth):
                        apendStr+= "8"
                    elif(sortedElement == nine):
                        apendStr+= "9"
                solution.append(apendStr)
    print(solution)
    print("hey")

if __name__ == '__main__':
    #partOne(puzzle_input)
    #partTow(puzzle_input)
    connectBrain(inPutFoRWierdWay1, puzzle_input)
