
with open("day5\input.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(" ") for line in puzzle_input.readlines()]
    #print(puzzle_input)
    
    


def partOne(lines):
    cords =[]
    cont1 = 0
    for elemnts in puzzle_input:
        x1 = int(elemnts[0].split(",",1)[0])
        y1 = int(elemnts[0].split(",",1)[1])
        x2 = int(elemnts[2].split(",",1)[0])
        y2 = int(elemnts[2].split(",",1)[1])
        print(x1, end="")
        print(y1)
        if(x1 == x2):
            if(y1 > y2):
                #print("bigger ")
                minus = y1 +1
                for i in range(minus-y2):
                    minus -=1
                    cords.append(str(x1) + "," + str(minus))
            else: 
                minus = y2 +1
                for i in range(minus-y1):
                    minus -=1
                    cords.append(str(x1)+ "," + str(minus))
                #print("smaller")
        elif(y1 == y2):
            if(x1 > x2):
                #print("bigger ")
                minus = x1 +1
                for i in range(minus-x2):
                    minus -=1
                    cords.append((str(minus) + "," +  str(y1)))
            else: 
                minus = x2 +1
                for i in range(minus-x1):
                    minus -=1
                    cords.append( str(minus)+ "," + str(y1)) 
        elif(x1 == y1 and x2 == y2 ) :
            if(x1 > x2):
                minus = x1 +1
                for i in range(minus-x1):
                    minus -=1
                    cords.append( str(minus)+ "," + str(minus))
            else:
                minus = x2 +1
                for i in range(minus-x1):
                    minus -=1
                    cords.append( str(minus)+ "," + str(minus))
        # elif(x1 +y1 == x2 +y2):
        #     if(x1 > x2):
        #         minus = x1+1
        #         plus =  x2 -1
        #         for i in range(minus-x1):
        #                 minus -=1
        #                 plus +=1
        #                 cords.append( str(minus)+ "," + str(plus))
            
                
                     
                
    print(cords)
    
    t = 10
    
    gridReal =[]
    
    for i in range(t):
        grid =[]
        for r in range(t):
            grid.append(".")
        gridReal.append(grid)
 
    #print(gridReal)
    
    for n in cords:
        workingN =str(n)
        x = workingN.split(",",1)[0]
        y = workingN.split(",",1)[1]
        x = int(x)
        y  =int(y)
        if(gridReal[y][x]== "."):
            gridReal[y][x] = "1"
        elif(gridReal[y][x]== "1"):
            gridReal[y][x] = "2"
            cont1 +=1
    
    for i in range(t):
        print()
        for r in range(t):
            print(gridReal[i][r], end="")
    print()
    print(cont1)
    

partOne(puzzle_input)
