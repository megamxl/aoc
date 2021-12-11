
with open("day9\input.txt") as puzzle_input:
    puzzle_input = [[nums.split(" ") for nums in line.rstrip("\n") ]for line in puzzle_input.readlines()]
    #print(puzzle_input)


adjustenValues= 0
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

def suroundingsWithcurrXandY(lines, x,y):
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
                    
with open("day9\input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

matrix = [[int(x) for x in line] for line in lines]

regions = []
def link(c1, c2):
    c1_region = None
    c2_region = None
    for x in range(len(regions)):
        if c1 in regions[x]:
            if c1_region is not None:
                raise ValueError("c1")
            c1_region = x
        if c2 in regions[x]:
            if c2_region is not None:
                raise ValueError("c2")
            c2_region = x
    if c1_region is None and c2_region is None:
        regions.append([c1, c2])
    if c1_region is not None and c2_region is None:
        regions[c1_region].append(c2)
    if c1_region is None and c2_region is not None:
        regions[c2_region].append(c1)
    if c1_region is not None and c2_region is not None and c1_region != c2_region:
        regions[c1_region] += regions[c2_region]
        regions[c2_region] = []


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 9:
            continue
        if y != 0 and matrix[x][y-1] != 9:
            link((x, y), (x, y-1))
        if y != len(matrix[x]) -1 and matrix[x][y+1] != 9:
            link((x, y), (x, y+1))
        if x != 0 and matrix[x-1][y] != 9:
            link((x, y), (x-1, y))
        if x != len(matrix) -1 and matrix[x+1][y] != 9:
            link((x, y), (x+1, y))

region_sizes = ([len(region) for region in regions if len(region) > 0])
region_sizes.sort(reverse=True)
print("eyo captain jack")
print(region_sizes[0] * region_sizes[1] * region_sizes[2])
   
        
if __name__ == '__main__':
    print(f"P1: {partOne(puzzle_input)}")
    
