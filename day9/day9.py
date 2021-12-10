
with open("day9\input.txt") as puzzle_input:
    puzzle_input = [[nums.split(" ") for nums in line.rstrip("\n") ]for line in puzzle_input.readlines()]
    #print(puzzle_input)

posOfLOws = []
   
def getCell(lines,x,y):
    if x >=0 and y >=0:
        try: 
            if(lines[x][y] != None): return lines[x][y]
        except:
            pass 
    
def suroundings(lines, x,y):
    up = getCell(lines,x,y-1)
    down = getCell(lines,x,y+1)
    left = getCell(lines,x-1,y)
    rigth =  getCell(lines,x+1,y)
    return up,down,left,rigth
   
def partOne(lines): 
    result = 0
    for i in range(len(lines)):
       for m in range(len(lines[0])): 
            sur =suroundings(lines,i,m)
            count = 0
            count2 = 0
            g =4
            for t in range(len(sur)):
                if(sur[t] != None):
                    if(int(lines[i][m][0]) < int(sur[t][0])):
                        count+=1
                else: count2+=1
            g  -= count2
            if count == g: 
                result += int(lines[i][m][0]) +1
                posOfLOws.append(str(i)+ "," +str(m))
    return result                 
                    
    #print(suroundings(lines,0,1))
    #print(lines[0][-1])
def partTow(lines, puz):
   pass

if __name__ == '__main__':
    print(f"P1: {partOne(puzzle_input)}")
    print(posOfLOws)
    #partTow(puzzle_input)
    pass
