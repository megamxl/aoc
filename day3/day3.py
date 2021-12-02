linesSmall = []
with open("C:/Users/gerha/Desktop/aoc 2021/day3/smalInput.txt") as f:
    linesSmall = f.readlines()
    for t in range(len(linesSmall)):
        linesSmall[t] = linesSmall[t].rstrip("\n")

lines = []
with open("C:/Users/gerha/Desktop/aoc 2021/day3/input.txt") as f:
    lines = f.readlines()
    for t in range(len(lines)):
        lines[t] = lines[t].rstrip("\n")


def partOne(lines):
    cont1 = 0
    for i in range(len(lines)):
        print(lines[i])
        
def partTow(lines):
    cont1 = 0
    for i in range(len(lines)):
        print(lines[i])
        
partOne(lines)
partTow(lines)
