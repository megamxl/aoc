
with open("day7\input.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(",") for line in puzzle_input.readlines()]
    newInput =[]
    for i in range (len(puzzle_input[0])):
        newInput.append(int(puzzle_input[0][i])) 
    
def partOne(lines):
    lines.sort()
    sol=[]
    for i in lines:
        x=0
        for t in lines: 
            x +=  abs((i- t))
        sol.append(x)
    print(min(sol))
            
    
                

def partTow(lines):
    lines.sort()
    sol=[]
    for i in lines:
        x=0
        for t in lines: 
            x+= (abs((i- t))) * ( abs((i- t))+1)/2
        sol.append(x)
    print(min(sol))
    

    
if __name__ == '__main__':
    partOne(newInput)
    partTow(newInput)
    