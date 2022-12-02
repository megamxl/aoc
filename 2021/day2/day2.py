linesSmall = []
with open("C:/Users/gerha/Desktop/aoc 2021/day2/smalInput.txt") as f:
    linesSmall = f.readlines()
    for t in range(len(linesSmall)):
        linesSmall[t] = linesSmall[t].rstrip("\n")

lines = []
with open("C:/Users/gerha/Desktop/aoc 2021/day2/input.txt") as f:
    lines = f.readlines()
    for t in range(len(lines)):
        lines[t] = lines[t].rstrip("\n")


sudepthstring = "forward"

def partOne(lines):
    cont1 = 0
    a =""
    hor=0
    depth= 0
    for i in range(len(lines)):
        if sudepthstring in lines[i]:
            a = str(lines[i])
            a =int((a[8:9]))
           
            hor= hor+ay
        else:
            if "down" in lines[i]:
                a = str(lines[i]).rstrip("\n").split(" ")
                depth += int(a[1])
            else:
                a = str(lines[i]).rstrip("\n").split(" ")
                depth -= int(a[1])
    print(depth*hor)
                
def partTow(lines):
    a =""
    hor=0
    aim = 0
    depth= 0
    for i in range(len(lines)):
        if sudepthstring in lines[i]:
            a = str(lines[i])
            a =int((a[8:9]))
           
            hor= hor+a
            depth += aim *a 
        else:
            if "down" in lines[i]:
                a = str(lines[i]).rstrip("\n").split(" ")
                aim += int(a[1])
            else:
                a = str(lines[i]).rstrip("\n").split(" ")
                aim -= int(a[1])
    print(hor *depth)
        
partOne(lines)
partTow(lines)