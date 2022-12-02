from itertools import product,starmap


with open("day11\input.txt") as puzzle_input:
    puzzle_input = [[int(nums) for nums in line.rstrip("\n")] for line in puzzle_input.readlines()]
    #print(puzzle_input)

X = 9
Y = 9
COUNT = 0

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if (-1 < x <= X and -1 < y <= Y and (x != x2 or y != y2) and (0 <= x2 <= X) and (0 <= y2 <= Y))]
   
def onlyChecking(lines,ligthedThisRound):
    for rows in range(len(lines)):
        for cols in range(len(lines[0])):
            if(lines[rows][cols] > 9):
                lines[rows][cols] = 0
                global COUNT
                COUNT+=1
                ligthedThisRound.append((rows,cols))
                neighbor = neighbors(rows,cols)
                for m in neighbor:
                    lines[m[0]][m[1]] += 1 
                
def CheckForNine(lines):
    for rows in range(len(lines)):
        for cols in range(len(lines[0])):
             if(lines[rows][cols] > 9):  return True
    return False

def CheckForOnlyZeros(lines):
    for rows in range(len(lines)):
        for cols in range(len(lines[0])):
             if(lines[rows][cols] != 0):  return False
    return True

def rec(lines,ligthedThisRound):
    bo = CheckForNine(lines)
    if(bo): 
        onlyChecking(lines,ligthedThisRound)
        rec(lines,ligthedThisRound)
    else: 
        pass
        
def partOne(lines):
    for iteration in range(100):
        ligthedThisRound = []
        for rows in range(len(lines)):
            for cols in range(len(lines[0])):
                lines[rows][cols] += 1
           
        for rows in range(len(lines)):
            for cols in range(len(lines[0])):   
                rec(lines,ligthedThisRound) 
            for x in ligthedThisRound:
                lines[x[0]][x[1]] = 0 
            ligthedThisRound.clear()    
             
    print("===============")
    for t in lines:
        print(t)
    print("===============")
        
    pass    

def partTow(lines):
    count = 1
    count2 = 100
    while(True):
        count2 += 1
        ligthedThisRound = []
        for rows in range(len(lines)):
            for cols in range(len(lines[0])):
                lines[rows][cols] += 1
           
        for rows in range(len(lines)):
            for cols in range(len(lines[0])):   
                rec(lines,ligthedThisRound) 
            for x in ligthedThisRound:
                lines[x[0]][x[1]] = 0 
            ligthedThisRound.clear() 
        
             
        finished = CheckForOnlyZeros(lines)
        if(not finished):
            count += 1
        else:
            print("===============")
            for t in lines:
                print(t)
            print("===============")
            break
    return count2
        

if __name__ == '__main__':
    partOne(puzzle_input)
    print(f"P1 {COUNT}")
    print(f"P2 {partTow(puzzle_input)}")
    pass
